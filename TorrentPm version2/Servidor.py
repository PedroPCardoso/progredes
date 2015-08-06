# Servidor
import socket

import base64
from Cliente import Cliente
import threading



class Servidor:
        def __init__(self):
                HOST = "localhost"
                PORT = 57001
                lista_clientes = []
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print "Escutando a porta..."
                s.bind((HOST,PORT))
                s.listen(1)
                print "Aceitando a conexao..."
                conn,addr= s.accept()
                lista_clientes.append(addr)
               # print "recebendo o arquivo..."
                arq = open('arquivuns.mp3','wb')
                c = Cliente()
                ho=str(addr[0])
                po=str(addr[1])

                while 1:

                        d=conn.recv(1024)
                        da=d.split(",")
                        print da
                        #dados=base64.standard_b64decode(d)
                        if da[0] == '1':
                                if  self.arquivo(da[1],c):
                                        #s.connect((ho,po))
                                        c.enviar_arquivo(s,da[1])
                                s.send("nao encontrado")

                        elif not d:
                                break
                        arq.write(d)

                print "saindo..."
                arq.close()
                conn.close()
        def arquivo(self,nome,c):
                lista=c.lista_arq()
                print lista
                for e in lista:
                        if e == nome:
                                return True
                return False
