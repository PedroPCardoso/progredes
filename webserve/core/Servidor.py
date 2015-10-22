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
                s.bind((HOST,PORT))
                s.listen(1)
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
                        #print da
                        print "ta no servidor"
                        #dados=base64.standard_b64decode(d)
                        arq = open('pergunta.xml','wb')
                        for i in da[0]:
                            arq.write(i)
                        arq.close()

                        c.string_xml("pergunta.xml",1)
                        arq = open('pergunta.xml','r')

                        c.enviar_arquivo(conn,"getHostsResponse.xml") # fazer a condição ainda, to mudando manualmente, se for get hosts é só mudar o nome do arquivo que deve ser enviado de volta
                        conn.close()
                        break

                        if i.endswith("</fileName></getFiles></p2pse>")==1:
                            c.enviar_arquivo(conn,"getfilesResponse.xml") # fazer a condição ainda, to mudando manualmente, se for get hosts é só mudar o nome do arquivo que deve ser enviado de volta
                            conn.close()
                            break

                        """
                        if da[1] == '3':
                                        if self.arquivo(da[1],c):
                                                 print "enviando o arquivo"
                                                 c.enviar_arquivo(conn,da[1])
                                                 conn.close()
                                        else:
                                                conn.send("NE")  #caso o arquivo nao seja encontrado
                                                break
                        if da[1] == '2':
                             #tentando enviar a lista de jogos aqui, solicitados pelo clieente la na classe cliente
                            #    texto=self.solicitaHost()
                                print texto
                                print " enviando resposta"
                                break
                        elif not d:
                            """
                print "saindo... do serve"
                conn.close()


        def arquivo(self,nome,c):
                lista=c.lista_arq()
                print lista
                for e in lista:
                        if e == nome:
                                return True
                return False
#nome do arquivo
        def savingHosts(self,ip, port): #quando se conectar a alguem chama essa func
                    arquivo = open('lista_ips.txt','a') #ler o txt antes e jogar no sets
                    texto=ip + ',' + port + "\n"
                    arquivo.write(texto)
                    arquivo.close()
        def solicitaHost(self):
                arquivo = open('lista_ips.txt','r') #ler o txt antes e jogar no sets
                lista = ""
                for e in arquivo.readlines():
                         lista+=str(e)
                return lista
