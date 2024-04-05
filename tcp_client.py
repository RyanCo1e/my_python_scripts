#!/usr/bin/python3
#Developed by nlh
import socket
from termcolor import colored
import re

srv_addr = input(colored("Enter the server address you want to connect: ", "blue"))
chk_ip = re.compile(r'(\d){1,3}.(\d){1,3}.(\d){1,3}.(\d){1,3}')
ip_valid = chk_ip.search(srv_addr)

hostname = ''#give a hostname

def srv_ip():
        if ip_valid != None:
                ip = srv_addr
                return ip
        elif srv_addr == hostname:
                ip = socket.gethostbyname(hostname)
                return ip
        elif ip_valid == None:
                print(colored("Enter again the valid server ip address....", 'red')) 
                exit(0)
        else:
                exit(0)

ip = srv_ip()

while True:
        port_num = int(input(colored("Enter the port number of the server you want to connect: ", "blue")))

        if 0 < port_num <=65535:
                port = port_num
                break
        elif port_num > 65535 or port_num == 0:
                print(colored("Enter again the valid port nuber between 1 and 65535!!", 'red'))
                continue


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.send(b'Hello,what are you doing now?')
        message = s.recv(1024)
print(f"We received this {message} from the server")
