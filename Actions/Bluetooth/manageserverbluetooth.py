import os
import logging
from time import sleep
from Actions.Bluetooth.managebluetooth import ManageBluetooth
from bluetooth import BluetoothSocket

class ManageServerBluetooth(ManageBluetooth):
    
    def __init__(self, HOST, PORT):
        ManageBluetooth.__init__(self)
        self.logger.info("Creating a BluetoothServerManager class")
        self.bsocket.bind((HOST,PORT))
        self.bsocket.listen(1)

    def startServer(self):
        try:
            self.logger.debug("The server is waiting for a device")
            self.conn_client, self.address = self.bsocket.accept()
            self.conn_client.send("Connection establish!")
            self.conn_client.setblocking(False)
            self.conn_client.settimeout(30)#time out after 30 sec
        except Exception as e:
            self.logger.error(e)

    def sendData(self, data):
        try:
            self.conn_client.send(data)
        except Exception as e:
            self.logger.error(e)
            self.conn_client.close()
            raise

    def stopThread(self):
        super(ManageServerBluetooth, self).stopThread()
        self.conn_client.close()
        self.logger.debug("conn_client closed")

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s")
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info("starting the program")
    serv = ManageServerBluetooth("", 1)
    try:
        serv.startServer()
        while True:serv.sendData("coucou")
    except:
        serv.stopThread()
        if serv.isAlive():serv.join()
        serv.closeConnection()
