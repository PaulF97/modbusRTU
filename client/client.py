# libraries
from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer


# declaration of client and connexion
client = ModbusSerialClient(method='rtu', baudrate=9600,bytesize = 8,port='/dev/ttyCLIENT', timeout=1)
client.connect()
print(client)



while True:

    # write to slave slave id initialized at 0x01 for communication operations
    toSend = input("enter a string to write in holding register : ")  # enter message to send
    toSendCoils = input("enter a integer to write in coils: ")  # enter message to send
    client.write_registers(0x9c42, toSend.encode(),0x01)  # write to address 40002 of holding register
    client.write_coils(15, int(toSendCoils),0x01) #write  to address 15 coil register