from socket import *
import os.path
import tempprobe
import datetime

serverPort = 12000 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to recieve requests on port {}".format(serverPort))

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048)
    parsed = list(map(lambda x: x.decode(), message.split(b'\r\n')))
    request = parsed[0].split(' ')
    print('request: ', ' '.join(request))
    
    if request[1] == '/':
        successMsg = ('HTTP/1.1 200 OK')
        t = datetime.datetime.now()
        response = "Temperature at {:02d}:{:02d}:{:02d} - {:.2f} F".format(t.hour, t.minute, t.second, tempprobe.get())
        print('response: ', successMsg)
        connectionSocket.send((successMsg + '\n\n' + response + '\n').encode())
    else:
        errorMsg = ('HTTP/1.1 404 NOT_FOUND')
        print('response: ', errorMsg)
        specificErr = ('File Not Found'.format(request[1][1:]))
        connectionSocket.send((errorMsg + '\n\n' + specificErr + '\n').encode())
    
    connectionSocket.close()
