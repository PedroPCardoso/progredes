#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.ioproject.com.br/posts/2015/01/multiclient-server-application-python/#.VUJf7dQViko

#Mudando o server2
#http://stackoverflow.com/questions/5520821/python-multithreaded-server

import base64
import socket
import threading
import struct
import string

class clientThread(threading.Thread):
    def __init__(self, serv):
        threading.Thread.__init__(self)
        self.server = serv
        self.clientList = []
        self.running = True
        print("Client thread created. . .")
    def run(self):
        print("Beginning client thread loop. . .")
        while self.running:
            for client in self.clientList:
                message = client.sock.recv(self.server.BUFFSIZE)
                if message != None and message != "":
                    client.update(message)

class clientObject(object):
    def __init__(self,clientInfo):
        self.sock = clientInfo[0]
        self.address = clientInfo[1]
    def update(self,message):
        self.sock.send("Testamundo.\r\n".encode())

class Server(object):
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 22084
        self.BUFFSIZE = 1024
        self.ADDRESS = (self.HOST,self.PORT)
        self.clientList = []
        self.running = True
        self.serverSock = socket.socket()
        self.serverSock.bind(self.ADDRESS)
        self.serverSock.listen(2)
        self.clientThread = clientThread(self)
        print("Starting client thread. . .")
        self.clientThread.start()
        print("Awaiting connections. . .")
        while self.running:
            clientInfo = self.serverSock.accept()
            print("Client connected from {}.".format(clientInfo[1]))
            self.clientThread.clientList.append(clientObject(clientInfo))

        self.serverSock.close()
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



   
''' def recevingMessage(xmlDecode):
        data = con.recv(BUFFER_SIZE)
       # if not data: break
        print "received data:", data
        con.send(data)  # echo
        con.close() #num entendi esse con
        
    def conectado(con, cliente):
        print 'Conectado por', cliente
        while True:
            msg = con.recv(1024)
            if not msg: break
            print cliente, msg
            break
                
    def closeConection():
        print 'Finalizando conexao do cliente', cliente
        conection.close()
        thread.exit()

    def dataDecode(xmlEncoded):
        file_decoded = base64.b64decode(xmlEncoded)
'''
