import socket
import threading

hote = ''
port = 25565

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connection...")
server_socket.bind((hote, port))
server_socket.listen(5)
print("The server is now connected on the port {}".format(port))

connected_clients = []

def accept():
    while True:
        client_socket, addr = server_socket.accept()
        connected_clients.append(client_socket)   

def receive():
    while True:
        for client in connected_clients:
            try:
                receive = client.recv(1024)
                print(receive.decode())
            except:
                print("Error")
                connected_clients.remove(client)
                pass

thread_1 = threading.Thread(target=accept)
thread_1.start()

thread_2 = threading.Thread(target=receive)
thread_2.start()

thread_1.join()
thread_2.join()

print("Closing connections")
for client in connected_clients:
    client.close()

print("Connections closed")
server_socket.close()