import serial



# from pymodbus.server import StartAsyncSerialServer
from pymodbus.server import (
    StartAsyncSerialServer,
    StartSerialServer,
    StartTcpServer,
    StartTlsServer,
    StartUdpServer,
)
# from pymodbus.device import ModbusDeviceIdentification
# from pymodbus.datastore import ModbusSequentialDataBlock
# from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext



# store = ModbusSlaveContext(di=ModbusSequentialDataBlock(0, [17]*100),
# co=ModbusSequentialDataBlock(0, [17]*100),
# hr=ModbusSequentialDataBlock(0, [17]*100),
# ir=ModbusSequentialDataBlock(0, [17]*100))


# context = ModbusServerContext(slaves=store, single=True)

# portSerialServer = serial.Serial('/dev/ttySERVER', 9600)
# print(portSerialServer)

server = StartSerialServer(method='rtu', port='/dev/ttySERVER', baudrate=9600)
server.start()
print(server)

    
