
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.server import StartSerialServer
import threading
from pymodbus.device import ModbusDeviceIdentification

from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore.remote import RemoteSlaveContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer, ModbusSocketFramer
# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #

import logging

# FORMAT = ('%(asctime)-15s %(threadName)-15s'
#           ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig()
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
    print("before")
    print("Number of threads running : " , threading.active_count()) 
    StartSerialServer(context = context1, method='rtu',port = '/dev/ttySERVER', baudrate=9600) # function runs in infinit loop..

if __name__ == "__main__":

    context = data()

    run = threading.Thread(target=run_server, args=(context,))
    
    run.start()
