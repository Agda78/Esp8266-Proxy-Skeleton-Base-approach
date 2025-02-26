# Utility libraries for communication
import socket
import time

# Port to contact the server
SOCKET_PORT = 80

# Communication management class for ESP8266
class ESP8266Proxy:
    def __init__(self, host, port=SOCKET_PORT):
        self.host = host
        self.port = port

    # Function to send and receive service requests from the server
    def send_request(self, request):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall((request + "\n").encode())
            time.sleep(0.5)
            response = s.recv(1024).decode().strip()
            return response
