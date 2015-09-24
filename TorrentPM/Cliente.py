# Cliente
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import base64
import glob
from threading import Thread
class Cliente:
        def __init__(self):
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                print "conectando com servidor..."
                #s.connect((HOST,PORT))
                #self.enviar(s)


 # tentando criar um servidor, para esperar a resposta de outro controller
        def enviar(self, escolha,nome):
                HOST='localhost' #coloca o host do servidor
                PORT=57001
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                print "conectando com servidor..."
                s.connect((HOST,PORT))
                texto=escolha+","+nome
                s.send(texto)
                print "Aceitando a conexao..."

                # con, addr = s.accept()
                arq = open('arquivuns.mp3','w+b') #abrindo o arquivo para escrever o dado recebido

                while True:
                        d=s.recv(1024)
                        if d== "NE":
                                print "O Host nao tem esse Arquivo"
                                break
                        da=d.split(',')
                        if da[0]=="2":
                                return d
                        arq.write(d)
                        #print d
                        if not d:
                                break
                print "gravando no arquivo"
                arq.close()
                s.close()


        def enviar_arquivo(self,conn, nome):
                print "abrindo arquivo..."
                arq= open(nome,'r+b')
                for i in arq.readlines():
                        #print i
                        #dado=base64.standard_b64encode(i)
                        conn.send(i)
                print "saindo..."
                arq.close()
                print "fechou"


        def lista_arq(self):
                arquivos = []   # pegando lista de arquivos mp3
                arquivos= glob.glob('*.mp3')
                #arquivos.append(glob.glob('*.txt'))

                return  arquivos
