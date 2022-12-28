#  manages the client code

import logging
import os

from pymodbus.client import ModbusSerialClient


_logger = logging.getLogger()

#  setup of the client
def setup_sync_client(args):
    if args == "serial":
        client = ModbusSerialClient(port="/dev/ttyCLIENT", baudrate=9600)
        return client
    else :
        print("you can only do serial communication")
    

#  send commands
def run_sync_client(client1, modbus_calls=None):
    _logger.info("### Client starting")
    client1.connect()
    
    if modbus_calls:
        modbus_calls(client1)
    client1.close()
    _logger.info("### End of Program")

if __name__ == "__main__":

    string = input("enter the mode : ")
    testclient = setup_sync_client(string)
    print("test mode", testclient)
    while True:
        run_sync_client(testclient)
        toSend = input("what do you want to send : ")
        testclient.write_register(40003, toSend)
    # data = testclient.write_registers(0x9000, 255)
