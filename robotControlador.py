import motorControlador
import socket
import time

class RobotControlador:
    motor_ctrl = None

    def __init__(self):
        self.motor_ctrl = motorControlador.MotorControlador()
    
    def nombre(self):
        return {"name": socket.gethostname()}


    # Cosicas del motor
    def adelante(self):
        return {"rc":self.motor_ctrl.avanzar()}

    def atras(self):
        return {"rc":self.motor_ctrl.retroceder()}

    def izquierda(self):
        return {"rc":self.motor_ctrl.izquierda()}

    def izquierdax(self):
        return {"rc":self.motor_ctrl.izquierdax()}

    def derecha(self):
        return {"rc":self.motor_ctrl.derecha()}

    def derechax(self):
        return {"rc":self.motor_ctrl.derechax()}

    def parar(self):
        return {"rc":self.motor_ctrl.parar()}



# Test
if __name__ == '__main__':
    robot = RobotControlador()
    print(robot.nombre())
    print(robot.adelante())
    time.sleep(2)
    print(robot.parar())