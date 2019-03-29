from socket import *
import time, sys

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(0,10):
  message = input('Input lowercase sentence: ')
  clientSocket.sendto(message.encode(), (serverName, serverPort))
  startTime = time.time()
  sequence_number = i
  try: 
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    endTime = time.time() - startTime
    print(modifiedMessage.decode(), "RTT: ",  endTime, sequence_number)
  except:
    print("Request Timed Out")
      

clientSocket.close()
sys.exit()