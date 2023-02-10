# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.server import StartSerialServer
import threading
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer
from pymodbus.device import ModbusDeviceIdentification
from multiprocessing import Queue, Process
import time


# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #

import logging

# FORMAT = ('%(message)-15s')
# # logging.basicConfig(format=FORMAT)
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)


# class CallbackDataBlock(ModbusSp   try:arseDataBlock):
#     def __init__(self, devices, queue):
 
#         self.devices = devices
#         self.queue = queue

#         values = {k: 0 for k in devices.keys()}
#         values[0xbeef] = len(values) 
#         super(CallbackDataBlock, self).__init__(values)

#     def setValues(self, address, value):
#         super(CallbackDataBlock, self).setValues(address, value)
#         self.queue.put((self.devices.get(address, None), value))

# def read_device_map(path):

#     devices = {}
#     with open(path, 'r') as stream:
#         for line in stream:
#             piece = line.strip().split(',')
#             devices[int(piece[0], 16)] = piece[1]
#     return devices


# def data():

#     store = ModbusSlaveContext(
#         co=ModbusSequentialDataBlock(0, [0]*100), # coils register
#         di=ModbusSequentialDataBlock(0, [0]*100), # discrete input
#         ir=ModbusSequentialDataBlock(0, [0]*100), # input register
#         hr=ModbusSequentialDataBlock(0,[12]*100)
#     )

#     context = ModbusServerContext(slaves=store, single=True)
#     return context

# def rescale_value(value):
#     s = 1 if value >= 50 else -1
#     c = value if value < 50 else (value - 50)
#     return s * (c * 64)

# def device_writer(queue):0
#     while True:
#         device, value = queue.get()
#         scaled = rescale_value(value[0])
#         log.debug("Write(%s) = %s" % (device, value))
#         if not device: continue


# def updating_writer(a):
#     """ A worker process that runs every so often and
#     updates live values of the context. It should be noted
#     that there is a race condition for the update.

#     :param arguments: The input arguments to the call
#     """
#     log.debug("updating the context")
#     context = a[0]
#     register = 3
#     slave_id = 0x00
#     address = 0x10
#     values = context[slave_id].getValues(register, address, count=5)
#     values = [v + 1 for v in values]
#     log.debug("new values: " + str(values))
#     context[slave_id].setValues(register, address, values)


class CustomDataBlock(ModbusSparseDataBlock):

    def setValues(self, address, value):
        super(CustomDataBlock, self).setValues(address, value)
        print("the value {} has been written to address {}".format(value, address-1))
    # def getValues(self, address, count=1):
    #     super(CustomDataBlock, self).getValues(address, count)
    #     print("getting the value{} from address {}".format(count, address-1))

# update the values send to the server
def updating(a):
    context = a[0]
    register = 0x03
    slave_id = 0x01
    address = 0x00
    values = context[slave_id].getValues(register, address, count=10)
    print(values)
    values = [v + 1 for v in values]
    context[slave_id].setValues(register, address, values)

def counter(cont, context):
    slave_id = 0x01
    flag_encenderCamaras = False
    while True:
        register = 3    
        address = 0
        values = context[slave_id].getValues(register, address, count=1)
        if values[0] == 1 and flag_encenderCamaras == False:
            flag_encenderCamaras = True
        elif values[0] == 2 and flag_encenderCamaras == True: 
            flag_encenderCamaras = False
        if flag_encenderCamaras == True:
            address = 0x00
            register = 10   
            print(cont)
            context[slave_id].setValues(register, address, [cont])
            cont = cont + 1 
            time.sleep(1)
def data():

    store = ModbusSlaveContext(
        co=ModbusSequentialDataBlock(0, [0]*100), # coils register
        di=ModbusSequentialDataBlock(0, [0]*100), # discrete input
        ir=ModbusSequentialDataBlock(0, [0]*100), # input register
        hr=ModbusSequentialDataBlock(0,[1]*100)
    )

    context = ModbusServerContext(slaves=store, single=True)
    return context

def run_callback_server():

    block  = CustomDataBlock([12]*100)
    
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


    hilo = threading.Thread(target=counter, args=(0,context))
    hilo.daemon = True
    hilo.start()

    print("Number of threads running : " , threading.active_count())
    updating(a=(context,))   
    StartSerialServer(context=context, framer=ModbusRtuFramer, identity=identity,data_block=block, port = '/dev/ttySERVER', baudrate=9600) # function runs in infinit loop..

if __name__ == "__main__":

    # context=data()
    run_callback_server()