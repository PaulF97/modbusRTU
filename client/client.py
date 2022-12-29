# libraries
from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
# declaration of client and connexion
client = ModbusSerialClient(method='rtu',port='/dev/ttyCLIENT')
client.connect()
print(client)



while True:
     toSend = input("enter a string to write in holding register : ")  # enter message to send
     toSendCoils = input("enter a integer to write in coils: ")  # enter message to send
     client.write_registers(40001,toSend.encode(),0x01)
     client.write_coil(13, True,0x01)
     client.write_coils(15, int(toSendCoils.encode()),0x01)
client.close()