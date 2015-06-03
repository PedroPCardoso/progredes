
import base64
import socket
import threading
import struct
import string


class clientObject(object):
    def __init__(self,clientInfo):
        self.sock = clientInfo[0]
        self.address = clientInfo[1]
    def update(self,message):
        self.sock.send("Testamundo.\r\n".encode())




class Server(object):
    def __init__(self):
        BUFFSIZE = 1024
        clientList = [] # lista de clientes, aonde serao guardadas as informaçoes do mesmo.
        running = True
        HOST = 'localhost'      # Symbolic name meaning all available interfaces
        PORT = 50007              # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        s.listen(2)
        print("Starting client thread. . .")
        print("Awaiting connections. . .")
        while running:
            clientInfo = s.accept()
            print("Client connected from {}.".format(clientInfo[1]))
            clientList.append(clientObject(clientInfo))
            print "funfa"
            print clientList
        s.close()
    

        print("- end -")
    def codificar64(Nmusica):
        sound_file = Nmusica
        # use mode = "rb" to read binary file
        fin = open(sound_file, "rb")
        binary_data = fin.read()
        fin.close()
        # Codificar para a base binaria
        b64_data = base64.b64encode(binary_data)
    def decodificar(codigo):
        # decode base64 string to original binary sound object
        mp3_data = base64.b64decode(b64_str)
  






serv = Server()