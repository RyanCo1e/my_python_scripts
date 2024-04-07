#Author: nlh
import socket
import sys
import os
from termcolor import colored
import time

def banner(ip, port):
        try:
                s = socket.socket()
                s.connect((ip, port))
                data = s.recv(1024)
                return str(data)
        except:
                return

def vuln_scan(banner_data, filename):
        file = open(filename, "r")
        for line in file.readlines():
                try:
                        if line.strip("\n") in banner_data:
                                print(colored(f"[+]The {banner_data} is vulnerable!", "white"))
                except:
                        exit(0)

if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
                print(colored(f"[-]{filename} does not exist!!", "red"))
                exit(0)
        if not os.access(filename, os.R_OK):
                print(colored("[-]Access denied!!!", "red"))
                exit(0)
        else:
                host = input(colored("[*]Enter the hostname you want to scan: ", "blue"))
                host_ip = socket.gethostbyname(host)

                for port in range(1,1000):
                        banner_data = banner(host_ip, port)
                        if not banner_data:
                                print(colored(f"[-]Unable to connect to Port {port}", "red"))
                        elif banner_data:
                                print(colored(f"[+]Port {port} is open\nWait..Let's check this port...","green"))
                                time.sleep(5)
                                vuln_scan(banner_data, filename)

else:
        print(colored("[-]Usage: "+ sys.argv[0] + " " + "Vulnerable_banners_list_file", "red"))
