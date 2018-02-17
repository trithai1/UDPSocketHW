# UDPPingerClient.py
from socket import *
import time

serverIP = "127.0.0.1"
serverPort = 12000

#Create a UDP socket: Internet Protocol V4, Datagram
clientSocket = socket(AF_INET, SOCK_DGRAM)

for k in range(1,11):
    try:
        sendTime = time.time()
        clientMessage = "Ping " + str(k) + " " + str(sendTime)
        clientSocket.sendto(clientMessage, (serverIP, serverPort))
        clientSocket.settimeout(1)
        serverMessage, address = clientSocket.recvfrom(1024)
        print(serverMessage + " RTT:" + str(time.time() - sendTime))
    except timeout:
        print "Request timed out"
        continue