import logging
from time import sleep
from gopigo import fwd, bwd, left, right, stop

class Move():
	def __init__(self):
		self.logger = logging.getLogger()
		self.logger.info("Creating movment class")
		self.degRot90 = 1.4

	def forward(self):
		self.logger.debug("The robot is moving forward")
		fwd()

	def backward(self, duration):
		self.logger.debug("The robot is going back")
		bwd()
		sleep(duration)#take care, the robot don't look at its back
		stop()

	def turnLeft(self):
		self.logger.debug("The robot turns left")
		left()
		sleep(self.degRot90)
		stop()
		
	def turnRight(self):
		self.logger.debug("The robot turns right")
		right()
		sleep(self.degRot90)
		stop()
