import socket
import time, sys

def Main():
  host = '127.0.0.1'
  port = 12000
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as clientSocket:
    clientSocket.settimeout(1)
    for i in range(0,10):
      message = input('Input lowercase sentence: ')
      clientSocket.sendto(message.encode(), (host, port))
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

if __name__ == '__main__':
  Main()