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
    #GPIO.setwarnings(False)
    #GPIO.cleanup()

    ''' configuro las 4 conexiones a puente H para controlar motor
    como output y a 0 '''
    for m in motors:
        print("Inciando pin ",m)
        GPIO.setup(m, GPIO.OUT, initial=GPIO.LOW)
    print("Estado de los pines tras iniciar...")
    check_pins()

def check_pins():
    for m in motors:
        estado = GPIO.input(m)
        print("Pin ", m, "->", estado)

def stop():
    logging.debug("Paramos el motor")
    for m in motors:      
        GPIO.output(m, GPIO.LOW)

def limpiar():
    stop()
    GPIO.cleanup()

def der_ad_on():
    logging.debug("Motor derecho adelante - ON")
    print("Motor derecho adelante - ON")
    GPIO.output(RF, GPIO.HIGH)

def der_ad_off():
    logging.debug("Motor derecho adelante - OFF")
    print("Motor derecho adelante - OFF")
    GPIO.output(RF, GPIO.LOW)

def izq_ad_on():
    logging.debug("Motor izquierdo adelante - ON")
    print("Motor izquierdo adelante - ON")
    GPIO.output(LF, GPIO.HIGH)

def izq_ad_off():
    logging.debug("Motor izquierdo adelante - OFF")
    print("Motor izquierdo adelante - OFF")
    GPIO.output(LF, GPIO.LOW)

# Atrás
def der_at_on():
    logging.debug("Motor derecho atrás - ON")
    print("Motor derecho atrás - ON")
    GPIO.output(RB, GPIO.HIGH)

def der_at_off():
    logging.debug("Motor derecho atrás - OFF")
    print("Motor derecho atrás - OFF")
    GPIO.output(RB, GPIO.LOW)

def izq_at_on():
    logging.debug("Motor izquierdo atrás - ON")
    print("Motor izquierdo atrás - ON")
    GPIO.output(LB, GPIO.HIGH)

def izq_at_off():
    logging.debug("Motor izquierdo atrás - OFF")
    print("Motor izquierdo atrás - OFF")
    GPIO.output(LB, GPIO.LOW)

# Giro izquierda
def giro_izq_on():
    print("Giro a la izquierda - ON")
    logging.debug("Giro a la izquierda - ON")
    der_ad_on()

def giro_izq_off():
    print("Giro a la izquierda - OFF")
    logging.debug("Giro a la izquierda - OFF")
    der_ad_off()

def giro_izq_super_on():
    logging.debug("Super giro a la izquierda - ON")
    der_ad_on()
    izq_at_on()

def giro_izq_super_off():
    logging.debug("Super giro a la izquierda - OFF")
    der_ad_off()
    izq_at_off()

# Giro derecha
def giro_der_on():
    logging.debug("Giro a la derecha - ON")
    izq_ad_on()

def giro_der_off():
    logging.debug("Giro a la derecha - OFF")
    izq_ad_off()

def giro_der_super_on():
    logging.debug("Super giro a la derecha - ON")
    izq_ad_on()
    der_at_on()

def giro_der_super_off():
    logging.debug("Super giro a la derecha - OFF")
    izq_ad_off()
    der_at_off()


def adelante(t=None):
    izq_ad_on()
    der_ad_on()
    if t:
        time.sleep(t)
        izq_ad_off()
        der_ad_off()

def atras(t=None):
    izq_at_on()
    der_at_on()
    if t:
        time.sleep(t)
        izq_at_off()
        der_at_off()


if __name__== '__main__':
    
    init()
    print("Adelante")
    adelante(2)
    time.sleep(1)

    print("Atrás")
    atras(2)
    time.sleep(1)

    # GIro izquierda
    print("Giro a la izquierda simple")
    giro_izq_on()
    time.sleep(1)
    giro_izq_off()
    time.sleep(1)

    # GIro derecha
    print("Giro a la derecha simple")
    giro_der_on()
    time.sleep(1)
    giro_der_off()
    time.sleep(1)

    # Supergiro a la izquierda
    print("Giro a la izquierda super")
    giro_izq_super_on()
    time.sleep(1)
    giro_izq_super_off()
    time.sleep(1)
    
    # Supergiro a la derecha
    print("Giro a la derecha super")
    giro_der_super_on()
    time.sleep(1)
    giro_der_super_off()
    time.sleep(1)

    stop()
    print("Estado de los pines tras parar...")
    check_pins()
    print("Outputs puestos a LOW, limpiamos GPIO")
    GPIO.cleanup()
