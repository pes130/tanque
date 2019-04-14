import RPi.GPIO as GPIO
import time
import logging
import constantes as ctes

LF = ctes.MOTOR_LF
LB = ctes.MOTOR_LB
RF = ctes.MOTOR_RF
RB = ctes.MOTOR_RB

motors = [RF, RB, LF, LB]

def init():
    logging.debug("Inicio del motor")
    print("Inicio del motor")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.cleanup()

    ''' configuro las 4 conexiones a puente H para controlar motor
    como output y a 0 '''
    for m in motors:
        GPIO.setup(m, GPIO.OUT)
        GPIO.setup(m, GPIO.LOW)

def stop():
    logging.debug("Paramos el motor")
    for m in motors:
        GPIO.setup(m, GPIO.LOW)

def der_ad_on():
    logging.debug("Motor derecho adelante - ON")
    GPIO.output(RF, GPIO.HIGH)

def der_ad_off():
    logging.debug("Motor derecho adelante - OFF")
    GPIO.output(RF, GPIO.LOW)

def izq_ad_on():
    logging.debug("Motor izquierdo adelante - ON")
    GPIO.output(LF, GPIO.HIGH)

def izq_ad_off():
    logging.debug("Motor izquierdo adelante - ON")
    GPIO.output(LF, GPIO.HIGH)



# Pruebas
def adelante(t):
    izq_ad_on()
    der_ad_on()
    time.sleep(t)
    izq_ad_off()
    der_ad_off()

if __name__== '__main__':
    init()
    adelante(2)
    stop()
    print("Prueba lista, paramos")
    GPIO.cleanup()
