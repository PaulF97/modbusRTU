This repository has two files that will simulate serial communication using Modbus protocol with help of pyModbus library functions. The final goal will be the emplimenation of a modbus library on a MCU. Modbus can read and write various informations about the PICO card.

The goal of this test will be to simulate communication by this protocole to then implemente a firmware contaning a Modbus slave device to the PICO. 
But before that, let's implement a master/slave communication between two linked serial ports on the PC.

First off all, we had to use a software to link our two serial ports, /dev/ttyCLIENT and /dev/ttySERVER.
To do this, we used socat software witch is designed for linkin two serial ports together by using the following command line : 

sudo socat -u -u pty,raw,echo=0,link=/dev/ttyCLIENT pty,raw,echo=0,link=/dev/ttySERVER. This command will run continusly unless we kill the process.

Once this is done, we can see that the serial ports are available by doing ls command in the /dev directory and we can design or client and server code.


We will use the Pymodbus library contaning various functions usefull to communicat between devices or serial ports such as opening initializing clients, servers, write or read into registers.

Since we want to do Modbus Serial communication, we will use RTU mode of the Modbus protocole.

To implement the server, first we need to import various pymodbus functions, and call the ModbusSerialClient() that will declare and initialize a serial client. This function takes in parameters the serial port (/dev/ttyCLIENT) and the method used witch is RTU for us. Note that we can pass additional parameters such as a timout value or the baudrate of the transaction.
Once this is done, we can start the server using the start() method and write commands to send to the server.

For this example, we want to write a string at the address 40001 of the holding register using the write_registers() methode and a number that will be written in the address 15 of coils registers.

The client is runned continuously unless we kill the process.

To see the data on the server side, we need to configure our server.




Then we use the function start() to open the client and send information to the server 





