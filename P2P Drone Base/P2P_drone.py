import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
import socket 
import sys
import time
print("DOING SOMETHING")
port = 5598
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
logging.debug("Stated sockets and imported modules")
print("STILL DOING SOMETHING")
try:
    logging.debug("Attempting to bind first time")
    s.bind(("",port))
    logging.debug("Bound successfully")
except :
    logging.error("Could not bind default socket 5598, retrying.", exc_info=True)
    for counts in range (3):
        try:
            s.bind(("",port))
            logging.info("Successfully bound to port 5598 after error, continuing with normal operations.", exec_info=True)
            time.sleep(1)
        except:
            logging.error("Switching to alternative port selection.", exc_info=True)
            break
        while port_found == 0:
            for ports in range(5599, 5603):
                try:
                    s.bind(("",ports))
                    ports = str(ports)
                    logging.info(f"Bound to the port {ports}")
                    port_found = 1
                except:
                    if ports == 5603:
                        logging.critical("COULD NOT BIND TO ANY PORTS, SHUTTING DOWN.")
                        sys.exit()
                    logging.info(f"Could not bind to the port {ports}")
while True:
    pass



