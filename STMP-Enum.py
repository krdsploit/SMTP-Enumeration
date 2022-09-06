import subprocess
import os
import time
from colorama import Fore, Back, Style
import socket
import urllib3
import requests



b3n1r = '''




░█─── █──█ █── ▀▀█ ░█─▄▀ █▀▀█ █▀▀▄ 　 ▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█ 
░█─── █──█ █── ▄▀─ ░█▀▄─ █▄▄▀ █──█ 　 ─░█── █▀▀ █▄▄█ █─▀─█ 
░█▄▄█ ─▀▀▀ ▀▀▀ ▀▀▀ ░█─░█ ▀─▀▀ ▀▀▀─ 　 ─░█── ▀▀▀ ▀──▀ ▀───▀


$ The Powerful SMTP Enumeration

$ Provided By Kurdish Pentester 
										'''
						

print("=====================================================================================================")

										

print(Fore.RED + b3n1r)

print(Fore.RED + "[!] Notice during using this tool this script requiers the some packages [!]")

time.sleep(0.6)

agr = input("[*] Do you want to installing the main packages for this tool [Y] + [ N ] [*]")

if agr=="Y":
   subprocess.call(['pip3','install','colorama'])

agr1 = input("[*] Do you want to installing the main packages for this tool [Y] + [ N ] [*]")

if agr1=="Y":
   subprocess.call(['pip3','install','smtp-user-enum'])

   
elif agr and agr1  =="N":
	quit()

print("===================================================================================================================================================")
	

time.sleep(0.6)
print("[-] We have to checking the connection between machine [-]")

time.sleep(0.10)
	
s = socket.socket()

try:
	s.connect(("IPTRG", "PORT_NUM"))
	
	time.sleep(0.3)
	print("[+] Connection Active [+]")
except:
	print(Fore.GREEN + "[+] Connection Not Active [+]")
	
print("===================================================================================================================================================")


def list_menu():
	time.sleep(0.5)
	print("[!] Checking User Exsit [!]")
	time.sleep(0.5)
	print("[!] Host Running The SMTP [!]")
	time.sleep(0.5)
	
	usr = int(input("Your Options ==> " ))
	
	if usr==1:
		ch()
	
		

def ch():
	subprocess.call(['smtp-user-enum','-M','VRFY','-u','bin','-t','IP_TRG'])


if __name__ == '__main__':
	list_menu()
	


