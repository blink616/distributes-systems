import socket
import pygame

lPort = 11222
lIP = "127.0.0.1"
BUFFER_SIZE = 1024

#function for creating message for clients
def createPlayerInfo(playerNumber, playerGraphic):
	return str.encode(str(playerNumber)+ "\t" + playerGraphic)

#function for parsing message received by clients
def breakdown(mes):
	spl = str.split(mes.decode("UTF-8"), sep = "\t", maxsplit=2)
	if(len(spl) == 1):
		spl.append("")
	return spl

if __name__ == "__main__":
	#list of current connected clients
	currentPlayer = {}
	currentGraphic = {}
	currentPlayerNumber = {}

	gameStart = False

	#UDP socket , setting up server
	UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)		#create a datagram socket
	UDPServerSocket.bind((lIP,lPort))		#bind the address and ip
	print("Server has started listening")

	#listen for incoming datagrams
	while gameStart == False:
		mes,addr = UDPServerSocket.recvfrom(BUFFER_SIZE)		#receiving messages
		playerID,mes = breakdown(mes)		#parsing message received
		#displaying message on server side
		print("Message from player:" + mes)
		print("player IP Address: " + playerID)

		#adding player to currentPlayer List
		#check ig player already in currentPlayer, then don't allow duplicate player
		if(playerID in currentPlayer.keys() and mes == "ADD"):
    			UDPServerSocket.sendto(str.encode("ERROR"), addr)

    	#check if new player: not already in currentPlayer list
		elif(playerID not in currentPlayer.keys() and mes == "ADD"):
			currentPlayer[playerID] = addr;
			UDPServerSocket.sendto(str.encode("OK"), addr)
			UDPServerSocket.sendto(str.encode(str(len(currentPlayer))), addr)
			currentPlayerNumber[playerID] = str(len(currentPlayer))
			print("Connection created with:" + playerID)

		#check if player wants to leave
		elif(playerID in currentPlayer.keys() and mes == "LEAVE"):
			currentPlayer.pop(playerID)

		if len(currentPlayer) == 3:
			gameStart = True
			for tempid, tempaddr in currentPlayer.items():
				UDPServerSocket.sendto(str.encode("GAME_START"),tempaddr)
    				
		else:
			for tempid, tempaddr in currentPlayer.items():
				UDPServerSocket.sendto(str.encode("WAIT_PLAYER"),tempaddr)

	#for all players in game, get graphics
	for x in range(0,len(currentPlayer)):
		mes,addr = UDPServerSocket.recvfrom(BUFFER_SIZE)		#receiving messages
		playerID,graphic = breakdown(mes)		#parsing message received
		#displaying message on server side
		print("player IP Address: " + playerID)	
		print("player graphic: " + graphic)
		currentGraphic[playerID] = graphic

	#broadcast all player graphics
	for tempid, tempaddr in currentPlayer.items():
		UDPServerSocket.sendto(str.encode(str(len(currentPlayer))),tempaddr) #send number of players
		for playerID, graphic in currentGraphic.items():	
			UDPServerSocket.sendto(createPlayerInfo(currentPlayerNumber[playerID], graphic),tempaddr)
    			
	#broadcast message 
	#if(playerID in currentPlayer.keys() and mes != ""):
		#for tempid, tempaddr in currentPlayer.items():
			#if (tempid != id):
				#UDPServerSocket.sendto(createMes(playerID, mes),tempaddr)