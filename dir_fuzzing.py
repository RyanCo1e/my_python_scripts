#Author: nlh

import sys
import requests
import socket
import os
from termcolor import colored
import time

try:
        url = sys.argv[1]
        wordlist = sys.argv[2]
        ext = sys.argv[3]
except:
        print("Usage: " + "url " + "wordlist " + "extension")
        exit()

print(colored("[*]Checking the url....", "blue"))
time.sleep(5)

try:
        s = socket.socket()
        status = s.connect_ex((url, 80))
        if not status:
                print("[+]The url works\n")
        else:
                print(colored("[-]Something wrong!Can't reach the remote server ", "red"))
                exit(1)
except:
        print(colored("\n[-]Connection fails - Make sure your url correct","red"))
        sys.exit(1)

print(colored("[*]Checking the wordlist...", "blue"))
time.sleep(5)

if not os.path.isfile(wordlist):
        print(colored("[-]File does not exist", "red"))
        sys.exit(1)
if not os.access(wordlist, os.R_OK):
        print(("[-]Access denied!!!", "red"))
        sys.exit(1)
else:
        print(colored("[+]Good Wordlist!\n", "white"))
        file = open(wordlist, 'r')
        for line in file.readlines()[14:]:
                dir = line.strip("\n")
                full_url = "http://" + url + "/" + dir + ext
                response = requests.get(full_url)
                if response.status_code == 200:
                        print(colored(f"{full_url} exists","green")) 
                else:
                        print(colored(f"{full_url} was Not found!!!",'red'))
