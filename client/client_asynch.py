import asyncio
import logging
import os

# --------------------------------------------------------------------------- #
# import the various client implementations
# --------------------------------------------------------------------------- #
from pymodbus.client import (
    AsyncModbusSerialClient,
)


_logger = logging.getLogger()


def setup_async_client(args):
    """Run client setup."""
    _logger.info("### Create client object")
    if args == "serial":
        client = AsyncModbusSerialClient(port="/dev/ttyCLIENT")
    return client
    
async def run_async_client(client1, modbus_calls=None):
    """Run sync client."""
    _logger.info("### Client starting")
    await client1.connect()
    assert client1.protocol
    if modbus_calls:
        await modbus_calls(client1)
    await client1.close()
    _logger.info("### End of Program")


if __name__ == "__main__":
  
    mode = input("what mode do you want (only serial ) : ")
    testclient = setup_async_client(mode)
    while True:
        asyncio.run(run_async_client(testclient), debug=True)