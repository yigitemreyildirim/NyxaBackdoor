import socket
from socket import command_interaction


class SocketListener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("listening on")
        (self.connection, address) = listener.accept()
        print("Connected from " + str(address))

    def command_interaction(self,command_input):
        self.connection.send(command_input)
        return self.connection.recv(1024)

    def listening(self):
        while True:
            command_input = raw_input("enter command: ")
            command_output = self.command_interaction(command_input)
            print(command_output)

socket_listener = SocketListener("192.168.1.59",8080)
socket_listener.listening()
