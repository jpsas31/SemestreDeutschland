import socket
import threading

HOST = "127.0.0.1"
PORT = 5002
clientInfo={}

def broadcast(msg,currentClient):
    global clientInfo
    for client in clientInfo.items():
        if(client[0] != currentClient):
            try:
                client[1].send(f"{currentClient}: {msg.decode()}".encode())
            except: 
                print('client is unreachable')


                
def handle_clients(newClient):
    
    newClient[0].send(f"hello client on address:{newClient[1]} \n please Input a nickname".encode())        
         
    with newClient[0]:
        
            print(f"Connected to {newClient[1]}")
            data = newClient[0].recv(1024)
            nickname= data.decode()
            clientInfo[nickname]=newClient[0]
            
            broadcast(f' joined the chat'.encode(), nickname)
            
            while True:
                # try:
                data = newClient[0].recv(1024)
                # except:
                   
                if(data == ''.encode()): 
                    del clientInfo[nickname]
                    print(f'Client on address:{newClient[1]} disconected')
                    broadcast(f'Client {nickname} disconected'.encode(), nickname)
                    break
               
                broadcast(data, nickname)
           
            
            
    
         
def createConnection(conn, addr):
    return threading.Thread(target=handle_clients, args=[(conn, addr)])

def accept_client_connection():
    print('waiting for clients')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as selectedSocket:
        selectedSocket.bind((HOST, PORT))
        selectedSocket.listen()
        while True:
            conn, addr = selectedSocket.accept()
            clientConn=createConnection(conn, addr)
            clientConn.start()
            # selectedSocket.close()
            # clientConn.join()
            # print('continue')
        
    
accept_client_connection()