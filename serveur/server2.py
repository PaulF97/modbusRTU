
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
import asyncio
from pymodbus.server import StartSerialServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from pymodbus.transaction import ModbusRtuFramer, ModbusBinaryFramer
# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #

import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_server():

# data store of the server
    store = ModbusSlaveContext(
        co=ModbusSequentialDataBlock(0, [0]*100), # coils register
        di=ModbusSequentialDataBlock(0, [0]*100), # discrete input
        ir=ModbusSequentialDataBlock(0, [15]*100), # input register
        hr=ModbusSequentialDataBlock(0, [16]*100) # holding
        )

    context = ModbusServerContext(slaves=store, single=True)

    print("before") 
    StartSerialServer(method='rtu',port = '/dev/ttySERVER', baudrate=9600) # function runs in infinit loop..

if __name__ == "__main__":
    run_server()