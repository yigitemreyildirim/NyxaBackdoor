import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listener.bind(("192.168.1.59",8080))
listener.listen(0)
print("listening on")
listener.accept()
print("Connected")
