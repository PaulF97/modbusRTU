# libraries
from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.constants import Defaults as ModbusDefaults

import logging
# FORMAT = ('%(message)-15s')
# logging.basicConfig(format=FORMAT)
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

# declaration of client and connexion

reading = 0
client = ModbusSerialClient(method='rtu', port = '/dev/ttyCLIENT', stopbits=1, bytesize=8, parity='N', baudrate=9600)

connexion = client.connect()
print(client)
print("\033[92m-------------------client connected----------------------\033[0m")


# log.debug("client started")

def responseReceived(response):
    print("connected")
#     log.debug("server has send data")


while True:
    
    if connexion == True:
        writeOrNot = input("Do you want to write in a address of holding register ?\n")

        if writeOrNot == "yes":
            value = input("enter the value :\n ")
            address = input("enter the address : \n")
            sendCustom = client.write_registers(int(address), int(value),0x01)
        
        print(" enter ID to get protocole ID \n enter IO to get the number of I/0 of the card \n enter PROBE what type is sond is the card")
        question = input("------ Witch information do you want to read ----------\n")

        if question == "ID":
            if writeOrNot =="yes":
                print("default value will be put back")
            sending = client.write_registers(0,1,0x01)  # write to address 49849 of holding register
            test = client.read_holding_registers(0,1,0x01)
            print("read from {} to {}".format(0,1+10-2))
            print(test)
        elif question == "I/O":
            if writeOrNot =="yes":
                print("default value will be put back")
            sending = client.write_register(1, 2,0x01)  # write to address 49849 of holding register
            test = client.read_holding_registers(1,1,0X01)
        elif question == "PROBE":
            if writeOrNot =="yes":
                print("default value will be put back")
            sending = client.write_register(2, 3,0x01)  # write to address 49849 of holding register
            test = client.read_holding_registers(2,1,0X01)
        else :
            print("you have not entered a good value")
    else:
        print("client not started")