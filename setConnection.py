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
    def breakdown(self, mes):
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
        self.response = ""
        name = playerName
        serport = (url, port)
        client = self.connection(name, serport)
        print("1")

        #create Threads for sending and receiving messages
        #publish = threading.Thread(target=self.sendMes, args=[client, serport])
        #subscribe = threading.Thread(target=self.receiveMes, args=[client,])

        #begin threading
        #publish.start()
        #subscribe.start()

    def connection(self, name, serport):
        clientID = name
        UDPClientSocket = socket.socket(family= socket.AF_INET,type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(self.createMes(clientID,"ADD"),serport)
        response, addr=UDPClientSocket.recvfrom(BUFFER_SIZE)

        #notify if connection established or not
        if response.decode("UTF-8") == "OK":
            print("Connection has been established")
            response, addr=UDPClientSocket.recvfrom(BUFFER_SIZE)
            print("You are player number ", response)
        else:
            print("Connection has been failed")
            os._exit()

        
        temp = {"clientID" : clientID, "socket" : UDPClientSocket}
        return temp

        

       

    

        