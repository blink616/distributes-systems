import pygame
import socket
import threading
import os

BUFFER_SIZE = 1024

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

class setConnection(object):

    #function for creating message for clients
    def createMes(self, clientID,mes=""):
        return str.encode(str(clientID)+ "\t" + mes)

    #function for parsing message received by clients
    def breakdownPlayerInfo(self, mes):
        spl = str.split(mes.decode("UTF-8"), sep="\t", maxsplit=2)
        if(len(spl) == 1):
            spl.append("")
        return spl
        
    #function to leave connection
    def leave(self, client,serport):
        client["socket"].sendto(self.createMes(client["clientID"], "LEAVE"), serport)
        print("Leaving chat")
        os._exit(1)


    #function to send message to server
    def sendMes(self, client,serport):
        while (True):
            tempStr = input("Enter Message: ")
            if tempStr == "LEAVE":
                self.leave(client, serport)
            client["socket"].sendto(self.createMes(client["clientID"], tempStr), serport)

    #receive broadcasted messages and display
    def receiveMes(self, client):
        while True: 
            resp, _ = client["socket"].recvfrom(BUFFER_SIZE)
            clientID, mes = self.breakdown(resp)

            print("\nMessage from: " + clientID)
            print(" == " + mes + "\n")

    def __init__(self,playerName, port, url):
        self.graphicset = {}
        self.clientID = playerName
        self.serport = (url, port)
        self.connection() # clientID, socket

        #create Threads for sending and receiving messages
        #publish = threading.Thread(target=self.sendMes, args=[client, serport])
        #subscribe = threading.Thread(target=self.receiveMes, args=[client,])

        #begin threading
        #publish.start()
        #subscribe.start()

    def connection(self):
        self.UDPClientSocket = socket.socket(family= socket.AF_INET,type=socket.SOCK_DGRAM)
        self.UDPClientSocket.sendto(self.createMes(self.clientID,"ADD"),self.serport)
        response, addr = self.UDPClientSocket.recvfrom(BUFFER_SIZE)

        #notify if connection established or not
        if response.decode("UTF-8") == "OK":
            print("Connection has been established")
            response, addr = self.UDPClientSocket.recvfrom(BUFFER_SIZE)
            self.playerNumber = int(response)
            print("You are player number ", response)
        else:
            print("Connection has been failed")
        
    def waitGame(self): #wait until another player is added
        while True:
            response, addr = self.UDPClientSocket.recvfrom(BUFFER_SIZE)
            if response.decode("UTF-8") == "GAME_START" :
                print("OTHER PLAYERS JOINED!")
                break
            elif response.decode("UTF-8") == "WAIT_PLAYER" :
                print("WAITING FOR OTHER PLAYERS")

    def sendGraphic(self, playerCharacter):  #sending character graphic to server
        self.UDPClientSocket.sendto(self.createMes(self.clientID,playerCharacter),self.serport)

    def receiveGraphic(self):   #receive other player character graphics from server
        response, addr = self.UDPClientSocket.recvfrom(BUFFER_SIZE)
        for x in range(0, int(response.decode("UTF-8"))):
            response, addr = self.UDPClientSocket.recvfrom(BUFFER_SIZE)
            graphicset = self.breakdownPlayerInfo(response)
            print("Player number: " + graphicset[0])
            print("Player graphic: "+ graphicset[1]) 
            self.graphicset[graphicset[0]] = graphicset[1]

    