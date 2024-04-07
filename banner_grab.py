#Developed by nlh
import socket
from termcolor import colored

def banner(ip, port):
        try:
                s = socket.socket()
                s.connect((ip, port))
                data = s.recv(1024)
                return data
        except:
                return 

host = input(colored("Enter the hostname you want to connect: ", "blue"))
host_ip = socket.gethostbyname(host)

for port in range(1,1000):
        banner_data = banner(host_ip, port)
        print(f"{banner_data} is received from port {port}")
