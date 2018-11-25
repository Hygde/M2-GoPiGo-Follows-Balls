import logging
from gopigo import *

class UsSensor():
	def __init__(self):
		self.logger = logging.getLogger()
		self.logger.info("Creating UsSensor class")
		
	def measure(self):
		self.logger.debug("Measure the distance with the us sensor")
		dist = us_dist(15)
		self.logger.info("Distance = %d"%dist)
		return dist

	def checkDist(self, dist):
		result = False
		if(dist > 15):
			self.logger.debug("Distance OK")
			result = True
		else:
			self.logger.debug("Distance LOW")
		return result
