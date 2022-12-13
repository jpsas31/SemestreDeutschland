import socket

HOST = "127.0.0.1"
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()
    conn, addr = socket.accept()
    with conn:
        print(f"Connected to {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())