import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listener.bind(("192.168.1.59",8080))
listener.listen(0)
print("listening on")
(connection,address) = listener.accept()
print("Connected from "+str(address))

while True:
    command_input = raw_input("enter command: ")
    connection.send(command_input)
    command_output = connection.recv(1024)
    print(command_output)
