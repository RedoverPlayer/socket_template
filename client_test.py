import socket

hote = "localhost"
port = 25565

connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connection...")
connection_with_server.connect((hote, port))
print("Connected on the port {}".format(port))

to_send_message = b""
while to_send_message != b"end":
    try:
    	to_send_message = input("> ")
    except:
    	print("Invalid message")
    	continue
    # Peut planter si vous tapez des caractères spéciaux
    to_send_message = to_send_message.encode()
    # On envoie le message
    connection_with_server.send(to_send_message)
    # msg_recu = connection_with_server.recv(1024)
    # print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

print("Closing the connection")
connection_with_server.close()