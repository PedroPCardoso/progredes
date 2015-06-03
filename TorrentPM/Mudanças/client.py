#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import base64

class client:
    HOST = ''     # Endereco IP do Servidor
    PORT = 40030           # Porta que o Servidor esta
    BUFFER_SIZE = 1024
    
    def __init__(self):
        HOST = 'localhost'    # The remote host
        BUFFER_SIZE = 1024
        PORT = 50007              # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send('Hello, world')

    def sendMessage(xmlEncode):
        conection.send(xmlEncode)
        print 'Mensagem Enviada!'
        print xmlEncode

    def closeConection():
        tcp.close()

    def encode(xml):
        file_encoded = base64.b64encode(xml) # ver como vai ser com arquivo



c=client()