#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://www.ioproject.com.br/posts/2015/01/multiclient-server-application-python/#.VUJf7dQViko
import socket
import thread
import select
import client
import base64

class server:

    def __init__(self):
        HOST = '127.0.0.1'                 # Interface que será utilizada
        PORT = 40030              # Número da porta que será "escutada"
        NUM_CLIENTS = 5

        inputs = []
        outputs = []

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))

        print('Listening to port {0}...'.format(PORT))
        sock.listen(5)

        inputs.append(sock) #Insere socket principal no inputs

        while True:

            try:
                inputready, outputready, exceptready = select.select(inputs, outputs, [])
            except select.error as e:
                break
            except socket.error as e:
                break

            for s in inputready:
                try:
                    if s == sock:
                        clientsock, address = sock.accept() #Aceita as conexões
                        outputs.append(clientsock)          #Adiciona à lista de outputs
                        inputs.append(clientsock)           #Adiciona à lista de inputs
                    else:
                        #Verify other sockets, already accepted.
                        data = s.recv(1024)                 #Recebe 1024 bytes
                        if data:
                            s.sendall(data)                 #Retorna os bytes recebidos ao cliente
                            print(data)
                        else:
                        #Caso não haja nenhum dado, significa que o cliente
                        #fechou a conexão
                            try:
                                s.close()
                                inputs.remove(s)
                                outputs.remove(s)
                            except BaseException as e:
                                pass
                except socket.error as e:
                    break
   

servidor = server()


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
