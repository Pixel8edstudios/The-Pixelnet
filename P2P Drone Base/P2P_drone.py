from P2P_Cogs.scanner_cogs.get_ip import *
import logging
import sys
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init
init(strip=not sys.stdout.isatty())
cprint(figlet_format('THE PIXELNET', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
print("PIXELNET V0.0.1 INITIALIZED")
console = logging.StreamHandler()
file_handler = logging.FileHandler("drone.log", "w")
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s: %(name)s: %(levelname)s: %(message)s',
    handlers = [file_handler, console]
)
import socket 
import time
address = get_ip()
logging.debug(f"THIS IS ADDRESS {address}")
port = 5598
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
logging.debug("Stated sockets and imported modules")
#TODO: Deal with FAILING MULTI-ADDRESS ACQUISITION IN LINUX

try:
    logging.debug("Attempting to bind first time")
    s.bind((address,port))
    logging.debug("Bound successfully")
except:
    logging.error("Could not bind default socket 5598, retrying.", exc_info=True)
    for counts in range (3):
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((address,port))
            logging.info("Successfully bound to port 5598 after error, continuing with normal operations.", exec_info=True)
            time.sleep(1)
        except:
            logging.error("Switching to alternative port selection.", exc_info=True)
            port_found = 0
            while port_found == 0:
                for ports in range(5599, 5604):
                    try:
                        logging.debug(ports)
                        s.bind((address,ports))
                        ports = str(ports)
                        logging.info(f"Bound to the port {ports}")
                        port_found = 1
                    except:
                        logging.info(f"Could not bind to the port {ports} with address {address}:{ports}")
                        if ports == 5603:
                            logging.critical("COULD NOT BIND TO ANY PORTS, SHUTTING DOWN.", exc_info=True)
                            sys.exit()

while True:
    time.sleep(1)