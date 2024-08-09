#!/bin/python3
import sys #system function
import socket
from datetime import datetime as dt

#Defining the target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
	#Translating a host name to IPV4
else:
	print("Invalid amount of arguments\nSyntax: python3 scanner.py <ip>")
	sys.exit()

print("-"*50)
print("Scanning target "+target)
print("Time started: "+str(dt.now()))
print("-"*50)
ports=[]
try:
	for port in range(50,85):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#AF_INET:IPV4 SOCK_STREAM: Port
		sock.settimeout(1)
		#connecting to the port
		result = sock.connect_ex((target,port))
		#returns error indicator
		if result == 0:
			print(f"Port {port} is open")
			ports.append(port)
		else:
			print(f"Port {port} is closed")
		sock.close()
		#closing the port after each iteration/attempt

except KeyboardInterrupt:
	print("\nExiting Program")
	sys.exit()

except socket.gaierror:
	print("\nHostname Couldnt be found!")
	sys.exit()

except socket.error:
	print("\nCouldnt connect to server.")
	sys.exit()

print("\nScanning complete.")	
if len(ports) == 0:
	print("\nNo open ports found.")
else:
	print("For Host {} the ports open are {}".format(target,ports))
