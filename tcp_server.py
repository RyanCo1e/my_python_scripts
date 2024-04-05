#!/usr/bin/python3
import socket
from termcolor import colored
import re
hostname = 'your_hostname'#Give a hostname 
def fun():
        ip_re = re.compile(r'(\d){1,3}.(\d){1,3}.(\d){1,3}.(\d){1,3}')
        srv_addr = input(colored("Enter your IP or HostName you want to host....", "blue"))
        right_ip = ip_re.search(srv_addr)
        if right_ip != None:
                ip = srv_addr
                return ip
        elif srv_addr == hostname:
                ip = socket.gethostbyname(hostname) 
                return ip
        elif right_ip == None:
                print(colored("Invalid IP address!!!\nTry Again....", "red"))
                exit(0)
        else:
                exit(0)

ip = fun()
or_port = input(colored("Enter the port number you want to listen....","blue"))
port = int(or_port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen()
        print(colored("Now we are listening your connection....", "green"))
        conn, addr = s.accept()
        data = conn.recv(1024)
        print(f"We have got this data:{data}")
        conn.sendall(data)
