# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
import socket

def Main():
  # CreateaUDP socket
  # Notice the use of SOCKDGRAM for UDP packets
  with socket.socket(socket.AF_INET , socket.SOCK_DGRAM) as serverSocket:
    # Assign IP address and port number to socket
    serverSocket.bind(('',12000))
    while True :
      print('Ready to ping...')
      # Generate random number in the range of0to 10
      rand = random.randint(0,10)
      # Receive the client packetalong with the address it is coming from
      message, address = serverSocket.recvfrom(1024)
      # Capitalize the message from the client
      message = message.upper()
      # If rand is less than 3, we consider the packet lost and do not respond
      if rand < 3:
        continue
      # Otherwise, the server responds
      serverSocket.sendto(message, address)

if __name__ == '__main__':
  Main()