import socket
import json
class MyClient():
    def __init__(self,host,port):
        self.HOST = host 
        self.PORT = port 
        self.commsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.commsocket.connect((self.HOST, self.PORT))
        
    def request(self,method,route,params={}):

        headers= json.dumps(params).replace('{','').replace('}','').replace(',','\r\n').replace('"','')
        headers= headers+ '\r\n\r\n'

        requestStr= f'{method} /{route} HTTP/1.0\r\n' + headers
    
        self.commsocket.sendall(requestStr.encode())
        try:
            return self.commsocket.recv(4096)
        except socket.error:
            return None




