import cv2
import logging
import numpy as np
from Actions.Detection.Camera.camera import Camera

class DetectCircle(Camera):

    def __init__(self):
        super(DetectCircle, self).__init__()
        self.logger.info("creating DetectCircle class")

    def detectCircle(self):
        img = self.getFrameFromCamera()
        circles = None
        if(not(img is None)):
            igray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            igray = cv2.GaussianBlur(igray,(5,5),0)
            igray = cv2.medianBlur(igray,5)
            igray = cv2.adaptiveThreshold(igray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,3.5)
            
            circles = cv2.HoughCircles(igray, cv2.HOUGH_GRADIENT, 1,2*len(igray),param1=30,param2=45,minRadius=0,maxRadius=0)
            
            if(circles is None):self.logger.debug("There is no circle in the pic")
            else:
                circles = np.round(circles[0, :]).astype("int")
                circles = circles[0]
                self.logger.debug(circles)
        return circles

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s")
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.debug("starting the program")

    cam = DetectCircle()
    cam.detectCircle()
    cam.closeCamera()
