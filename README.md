This repository has two files that will simulate serial communication using Modbus protocol with help of pyModbus library functions. The final goal will be the emplimenation of a modbus library on a MCU represented by the RP2040. Modbus can read and write various informations about the PICO card.

The goal of this test will be to simulate communication by this protocole to then implemente a firmware contaning a Modbus slave device to the PICO. 
But before that, let's implement a master/slave communication between two linked serial ports on the PC.

First off all, we had to use a software to link our two serial ports, /dev/ttyCLIENT and /dev/ttySERVER.
To do this, we used socat software witch is designed for linkin two serial ports together by using the following command line : 

sudo socat -u -u pty,raw,echo=0,link=/dev/ttyCLIENT pty,raw,echo=0,link=/dev/ttySERVER. This command will run continusly unless we kill the process.

Once this is done, we can see that the serial ports are available by doing ls command in the /dev directory and we can design or client and server code.


We will use the Pymodbus library contaning various functions usefull to communicat between devices or serial ports such as opening initializing clients, servers, write or read into registers. Modbus has 4 types of registers.

Coils registers : address from 0001 to 09999 access read and write. 1 bit space
Discrete Input : address from 10001 to 19999 access read only. 1 bit space
Input Register : address from 30001 to 39999 access read only. 16 bits space
Holding register : address from 40001 to 49999 access read and write. 16 bits space

For this test, we will only work with the coils and holding registers. But for the implementation of the protocole to the MCU, we will use all registers write and read data from the MCU.

Since we want to do Modbus Serial communication, we will use RTU mode of the Modbus protocole.

To implement the client, first we need to import various pymodbus functions, and call the ModbusSerialClient() that will declare and initialize a serial client. This function takes in parameters the serial port (/dev/ttyCLIENT) and the method used witch is RTU for us. Note that we can pass additional parameters such as a timout value or the baudrate of the transaction.
Once this is done, we can start the server using the start() method and write commands to send to the server.

Then in the infinite loop of the client, the user will prompt the data from the terminal to be send to the server thanks to the input python function.

Regardless of the server, we created a data store witch will help the server to read the information to the registers. Then, the function 
StartSerialServer() will be runed infinitely and it will receive the data from the client and print the data according to the RTU format.

To do the test, first we have to link the serial ports by using the command written above. Then we have to modify the writes of the serial ports to have the write and read access using the command chmod 777 <serial_port>. Per default, the user has no read and write access.

Then we have to lunch the server. To make sure the server has been correctly launch, the user must have the following message :


![image](https://user-images.githubusercontent.com/65350546/210055080-e7338223-54c4-4c42-9cbb-f36d3a4ba22c.png)


Once the server is launched, we can run the client.
In the client, we have initialized the slave ID at one, and it will be passed in the parameters of the write functions. Note that this is a optional parameter.

The code will ask the user to input a string and a integer that will be written to the data and coil register.


![image](https://user-images.githubusercontent.com/65350546/210055535-68e3c2e2-fe71-4dcd-bb70-c8c2a4617cb5.png)

The string will be passed to write_registers() function (function code 0x10)
The integer will be passed to the write_coils function (function code 0x0F)


In the terminal of the server, we can see two frames respecting the RTU Application Data Unit Format.


![image](https://user-images.githubusercontent.com/65350546/210055931-8e15bcaf-c190-4735-bda3-84b4fe7db0f0.png)


The frame has the following organisation : 

id slave : 1 byte
function code 2 bytes
start address : 2 bytes
size : 2 bytes
data : 8 bytes
CRC : 2 bytes



Same for the second frame, we can see that the slave ID is 0x01 and the function code 0x0F.

To check that the frame is properly send, the frame can be decoded on this link : 

https://rapidscada.net/modbus/









