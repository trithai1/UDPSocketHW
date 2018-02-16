# UDPPingerClient.py
from socket import *

#Create a UDP socket: Internet Protocol V4, Datagram
clientSocket = socket(AF_INET, SOCK_DGRAM)