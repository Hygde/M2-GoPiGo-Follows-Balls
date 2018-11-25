import os
import bluetooth
import logging
from threading import Thread
from bluetooth import BluetoothSocket, RFCOMM, discover_devices

class ManageBluetooth(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.logger = logging.getLogger()
        self.logger.info("Creating ManageBluetooth instance")
        self.bsocket = BluetoothSocket(RFCOMM)
        self.continuer = True

    def stopThread(self):
        self.continuer = False
        self.closeConnection()
        self.logger.debug("continuer set to False")

    def enabbleBluetooth(self):
        self.logger.debug("Try to enable bluetooth")
        os.system("rfkill block bluetooth")
        os.system("rfkill unblock bluetooth")

    def closeConnection(self):
        self.logger.debug("Closing the socket")
        self.bsocket.close()
        