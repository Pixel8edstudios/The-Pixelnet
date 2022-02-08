import socket 
import logging
import time
import random
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.critical("NOTE")
port = 5598
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind(("",port))
except :
    logging.error("Could not bind default socket 5598, retrying.", exc_info=True)
    for counts in range (3):
        try:
            s.bind(("",port))
            logging.info("Successfully bound to port 5598 after error, continuing with normal operations.", exec_info=True)
            time.sleep(1)
        except:
            logging.error("Switching to randomized port selection", exc_info=True)
            break
        for counts in range (3):
            
    


