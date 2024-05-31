import socket
import threading
 
HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Whatever IP address you found from running ifconfig in terminal.
# SERVER = ""
SERVER = socket.gethostbyname(socket.gethostname())
 
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Officially connecting to the server.
client.connect(ADDR)
 
def send():
    while True:
        msg = input('')
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        if msg == DISCONNECT_MESSAGE:
            break
               
def receive():
    while True:
        print(client.recv(2048).decode(FORMAT))
   
 
send_thread = threading.Thread(target=send)
receive_thread = threading.Thread(target=receive)
 
send_thread.start()
receive_thread.start()
 
# send("Hello World")
# input()
# send("Hello Matt")
# input()
# send("Hello Everyone")
# input()
# send(DISCONNECT_MESSAGE)