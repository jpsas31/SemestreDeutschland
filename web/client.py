import socket

HOST = "127.0.0.1" 
PORT = 5001 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    
    socket.connect((HOST, PORT))
    while True:
        socket.sendall(b"client message")
        data = socket.recv(1024)

        print(f"Received data: {str(data)}")