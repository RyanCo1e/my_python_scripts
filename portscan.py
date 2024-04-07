#Developed by nlh

import socket
from termcolor import colored
import time

open_ports = []

status = False


host = input(colored("Enter the hostname you want to scan: ", 'blue'))
host_ip = socket.gethostbyname(host)

start_time = time.time()

for port in range(1,1000):
        try:
                s = socket.socket()
                s.connect((host_ip, port))
                status = True
        except:
                status = False

        if status == True:
                print(colored(f"{port} is open", "white"))
                open_ports.append(port)
        else:
                print(colored(f"{port} is closed", "red"))

end_time = time.time()
time_taken = end_time-start_time
print("The open ports are:",open_ports)
print(colored(f"It took about {round(time_taken, 2)} seconds to scan!!", "white"))
