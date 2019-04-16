import Motor
import time



class MotorControlador():
    
    def __init__(self):
        print("Creamos instancia de motor controlador....")
        Motor.init()

    def __del__(self):
        print("Destruimos objeto Motor controlador...")
        Motor.limpiar()
    
    def avanzar(self):
        Motor.adelante()
        return True
    def retroceder(self):
        Motor.atras()
        return True
    
    def parar(self):
        Motor.stop()
        return True
    
    def izquierda(self):
        Motor.giro_izq_on()
        return True

    def izquierdax(self):
        Motor.giro_izq_super_on()
        return True

    def derecha(self):
        Motor.giro_der_on()
        return True

    def derechax(self):
        Motor.giro_der_super_on()
        return True


if __name__ == '__main__':
    
    m = MotorControlador()
    print("------ Izquierda ")
    m.izquierdax()
    time.sleep(1)
    m.parar()
    print("------ Derecha ")
    m.derechax()
    time.sleep(1)
    m.parar()
    time.sleep(5)
    print("------ Avanzamos ")
    m.avanzar()
    time.sleep(2)
    print("------ Parar ")
    m.parar()
   
  #  time.sleep(5)
   # print("------ Derecha ")
    #m.derechax()

    

    



    
    