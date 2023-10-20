import sys
import os
import time
import datetime
from Scan import spider

os.system('clear')

time.sleep(0.5)
RED = '\033[91m'

    
print(RED+'''
██████╗  ██████╗ ██████╗ ████████╗███████╗██████╗ ██╗██████╗ ███████╗██████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║   ███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║   ███████║██║     ██║██████╔╝███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                             v1.0 by Soyedi
    ''')
    
time.sleep(0.5);

print("Welcome ", end='', flush=True)
time.sleep(0.3)
print("in ", end='', flush=True)
time.sleep(0.3)
print("port ", end='', flush=True)
time.sleep(0.3)
print("scanner ", end='', flush=True)
time.sleep(0.3)
print("tool \n")

host = input("Target IP: ")  

time.sleep(0.6)
#banner
print('_'*50)
print("scanning Target"  + host)
print("scanning start " + str(datetime.datetime.now()))
print('_'*50)

spider(host)

