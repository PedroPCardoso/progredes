#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

import base64
from Cliente import Cliente
import threading

class Servidor:

        def __init__(self, HOST ,PORT):

                #listaclientes =[]

                lista_clientes = []
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print "Escutando a porta..."
                s.bind((HOST,PORT))
                s.listen(1)
                print "Aceitando a conexao..."
                conn,addr= s.accept()
                print addr
                lista_clientes.append(addr)
                # print "recebendo o arquivo..."
                c = Cliente()
                ho=addr[0] #host
                po=str(addr[1]) #porta do cliente
                self.savingHosts(ho,po)
                while 1:
                        d=conn.recv(1024)
                        print(d)
                        da=d.split(",")
                        print da
                        #dados=base64.standard_b64decode(d)
                        if da[0] == '3':
                                        if self.arquivo(da[1],c):
                                        #s.connect((ho,po))
                                       # conn.send("recebeu")
                                                 print "enviando o arquivo"
                                                 c.enviar_arquivo(conn,da[1])
                                                 conn.close()
                                        else:
                                                conn.send("NE")  #caso o arquivo nao seja encontrado
                                                break
                        if da[0] == '2':
                                text= self.solicitaHost()
                                print text
                                conn.send("2"+","+text)
                                break
                        elif not d:
                                break

                print "saindo..."


        def arquivo(self,nome,c):
                lista=c.lista_arq()
                print lista
                for e in lista:
                        if e == nome:
                                return True
                return False
#nome do arquivo
        def savingHosts(self,ip, port): #quando se conectar a alguem chama essa funç
                    arquivo = open('lista_ips.txt','a') #ler o txt antes e jogar no sets
                    texto=ip + ',' + port
                    arquivo.write(texto)
                    arquivo.close()
        def solicitaHost(self):
                arquivo = open('lista_ips.txt','r') #ler o txt antes e jogar no sets
                lista = ""
                print "solicita"
                print arquivo.readline()
                for e in arquivo.readlines():
                         lista=+str(e)
                return lista