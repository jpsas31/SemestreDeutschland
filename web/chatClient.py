import socket
import threading
import queue
HOST = "127.0.0.1" 
PORT = 5002

def listen(socket):
    while True:
        data = socket.recv(1024)
        if(data == ''.encode()): 
            print('server is unreachable')
            socket.close()
            break
        
        print(data.decode(), flush=True, end='\n>')
        
       
    
msgq=queue.Queue()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    threading.Thread(target=listen, args=[socket]).start()
    while True: 
        msg=input('>')
        try:
            socket.sendall(msg.encode())
        except:
            print('connection lost')
            break