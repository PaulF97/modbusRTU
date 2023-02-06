# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.server import StartSerialServer
import threading
from pymodbus.device import ModbusDeviceIdentification
import os
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
# from pymodbus.transaction import ModbusRtuFramer



# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #

import logging

FORMAT = ('%(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def data():
# data store of the server
    store = ModbusSlaveContext(
        co=ModbusSequentialDataBlock(0, [0]*100), # coils register
        di=ModbusSequentialDataBlock(0, [0]*100), # discrete input
        ir=ModbusSequentialDataBlock(0, [0]*100), # input register
        hr=ModbusSequentialDataBlock(0, [0]*100) # holding
        )

    context = ModbusServerContext(slaves=store, single=True)
    return context


def run_server(context1):
    identity1 = ModbusDeviceIdentification()
    identity1.VendorName = 'Pymodbus'
    identity1.ProductCode = 'PM'
    identity1.VendorUrl = 'https://github.com/paulhfisher/modbusRTU.git'
    identity1.ProductName = 'Pymodbus Server'
    identity1.ModelName = 'Pymodbus Server'
    identity1.MajorMinorRevision = '1.5'

    
    print("Number of threads running : " , threading.active_count())
    # os.system("sudo cat /dev/ttySERVER") 
    StartSerialServer(context = context1, identity = identity1, port = '/dev/ttySERVER', baudrate=9600) # function runs in infinit loop..

if __name__ == "__main__":
    
    context = data()
    run = threading.Thread(target=run_server, args=(context,))
    run.start()