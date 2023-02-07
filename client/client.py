# libraries
from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer

import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# declaration of client and connexion
client = ModbusSerialClient(method='rtu', baudrate=9600,bytesize = 8,port='/dev/ttyCLIENT', timeout=1)
connexion = client.connect()
print(client)


while True:

    if connexion == True:
        toSend = input("enter a string to write in holding register : ") # enter message to send
        toSendCoils = input("enter a integer to write in coils: ")  # enter message to send

        client.write_registers(49849, toSend.encode('ascii'),0x01)  # write to address 49849 of holding register
        client.write_coils(15, toSendCoils.encode('ascii'),0x01) #write  to address 15 coil register