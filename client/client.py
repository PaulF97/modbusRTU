# libraries
from pymodbus.client import ModbusSerialClient


# declaration of client and connexion
client = ModbusSerialClient(method='rtu', port='/dev/ttyCLIENT', baudrate=9600)
client.connect()
print(client)



while True:
    toSend = input("enter a command : ")  # enter message to send
    client.write_registers(40001,toSend.encode()) # send the message

client.close()
