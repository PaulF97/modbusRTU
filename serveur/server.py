# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.server import StartSerialServer
import threading
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.device import ModbusDeviceIdentification
import time

# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #

import logging

# FORMAT = ('%(message)-15s')
# # logging.basicConfig(format=FORMAT)
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)


class CustomDataBlock(ModbusSparseDataBlock):

    def __init__(self, values=None, mutable=True):
        super().__init__(values, mutable)

    # set values from datastore
    def setValues(self, address, value):
        super(CustomDataBlock, self).setValues(address, value)
        print("the value {} has been written to address {}".format(value, address-1))
    def getValues(self, address, count=1):
        return super().getValues(address, count)


# update the values send to the server
def updatingValues(a):
    context = a[0]
    register = 0x03
    slave_id = 0x01
    address = 0x00
    count = 10
    # values = context[slave_id].getValues(register, address, count)
    # print("the value is {}".format(values))
    # # values = [v + 1 for v in values]
    # # context[slave_id].setValues(register, address, values)

def counter(cont, context):
    slave_id = 0x01
    flag = False
    while True:
        register = 0x03    
        addressID = 0
        addressIO = 1
        addressPROBE = 2
        values = context[slave_id].getValues(register, addressIO, count=1)
        print("the value is {}".format(values))
        time.sleep(1)
        if values == 1 and flag == False:
            time.sleep(1)
            flag = True
        elif values == 2 and flag == True: 
            flag = False
        if flag == True:
            address = 0x00
            register = 1  
            print("test",cont)
            context[slave_id].setValues(register, address, [cont])
            cont = cont + 1 
            time.sleep(1)


def run_callback_server():

    block  = CustomDataBlock([0]*100)
    
    slaves  = {
        0x01: ModbusSlaveContext(di=block, co=block, hr=block, ir=block),
    }
    context = ModbusServerContext(slaves=slaves, single=False)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'https://github.com/paulhfisher/modbusRTU.git'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = '1.5'


    pid_background = threading.Thread(target=counter, args=(0,context))
    pid_background.daemon = True
    pid_background.start()

    print("Number of threads running : " , threading.active_count())
    updatingValues(a=(context,))
    print("\033[92mstarting server\033[0m")  
    StartSerialServer(context=context, framer=ModbusRtuFramer, identity=identity, port = '/dev/ttySERVER', baudrate=9600) # function runs in infinit loop..

if __name__ == "__main__":

    run_callback_server()