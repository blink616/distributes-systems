import socket
import pygame

lPort = 11222
lIP = "127.0.0.1"
BUFFER_SIZE = 1024

#function for creating message for clients
def createMes(clientID,mes=""):
	return str.encode(str(clientID)+ "\t" + mes)

#function for parsing message received by clients
def breakdown(mes):
	spl = str.split(mes.decode("UTF-8"), sep = "\t", maxsplit=2)
	if(len(spl) == 1):
		spl.append("")
	return spl

if __name__ == "__main__":
	#list of current connected clients
	currentClient = {}

	#UDP socket , setting up server
	UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)		#create a datagram socket
	UDPServerSocket.bind((lIP,lPort))		#bind the address and ip
	print("Server has started listening")

	#listen for incoming datagrams
	while(True):
		mes,addr = UDPServerSocket.recvfrom(BUFFER_SIZE)		#receiving messages
		clientID,mes = breakdown(mes)		#parsing message received
		print("11")
		#displaying message on server side
		print("Message from Client:" + mes)
		print("Client IP Address: " + clientID)

		#adding client to currentClient List

		#check ig client already in currentClient, then don't allow duplicate client
		if(clientID in currentClient.keys() and mes == "ADD"):
    			UDPServerSocket.sendto(str.encode("ERROR"), addr)

    	#check if new client: not already in currentClient list
		elif(clientID not in currentClient.keys() and mes == "ADD"):
			currentClient[clientID] = addr;
			UDPServerSocket.sendto(str.encode("OK"), addr)
			UDPServerSocket.sendto(str.encode(str(len(currentClient))), addr)
			print("Connection created with:" + clientID)

		#check if client wants to leave
		elif(clientID in currentClient.keys() and mes == "LEAVE"):
			currentClient.pop(clientID)

		#broadcast message 
		elif(clientID in currentClient.keys() and mes != ""):
			for tempid, tempaddr in currentClient.items():
				if (tempid != id):
					UDPServerSocket.sendto(createMes(clientID, mes),tempaddr)