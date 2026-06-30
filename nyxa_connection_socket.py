import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect(("192.168.1.59", 8080))

connection.send("connection ok")
