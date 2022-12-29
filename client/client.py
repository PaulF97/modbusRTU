# libraries
from pymodbus.client import ModbusSerialClient


# declaration of client and connexion
client = ModbusSerialClient(method='rtu',port='/dev/ttyCLIENT')
client.connect()
print(client)



while True:
     toSend = input("enter a command : ")  # enter message to send
    #  client.write_coil(3,True)# send the message
    #  client.write_coil(40001,int(toSend.encode())) # send the message
     client.write_registers(40001,toSend.encode())
client.close()