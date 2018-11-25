import logging
from time import sleep
from gopigo import stop
from Actions.Movement.move import Move
from Actions.Detection.USSensor.ussensor import UsSensor
from Actions.Detection.Camera.detectcircle import DetectCircle
from Actions.Bluetooth.manageserverbluetooth import ManageServerBluetooth

class Robot:
	def __init__(self):
		self.logger = logging.getLogger()
		self.logger.info("Creating the Robot class")
		
	def initRobot(self):
		self.logger.info("Initializing the robot")
		self.us = UsSensor()
		self.cam = DetectCircle()
		self.movement = Move()
		self.bserver = ManageServerBluetooth("",1)
		self.bserver.startServer()#wait here until a device is connected
		
	def start(self):
                self.logger.info("The robot enter in the while loop")
                count = 0
                try:
                        while(True):
                                circle = self.cam.detectCircle()
                                if circle is not None:
                                        self.bserver.sendData("Circle = "+str(circle[0])+";"+str(circle[1])+";"+str(circle[2]))
                                        dist = self.us.measure()
                                        self.bserver.sendData("Distance = %d"%dist)
                                        if(self.us.checkDist(dist)):self.movement.forward()
                                        else: stop()
                                else:
                                        stop()
                                        if count < 3:#it takes 3 frames before turning right
                                                count +=1
                                        else:
                                                count = 0
                                                self.movement.turnRight()                                        
                except Exception as e:
                        self.logger.error(e)

def initLogger():
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s")
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	ch.setFormatter(formatter)
	logger.addHandler(ch)
	return logger

if __name__ == "__main__":
	try:
		logger = initLogger()
		logger.info("starting program")
		robot = Robot()
		robot.initRobot()
		robot.start()
	except:
		stop()
		
