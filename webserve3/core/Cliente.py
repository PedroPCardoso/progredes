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


 #envia um pedido para outro servidor, e esperando a resposta do mesmo
        def enviar(self, escolha,nome):
                HOST='localhost' #coloca o host do servidor
                PORT=57001
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                print "conectando com servidor..."
                s.connect((HOST,PORT))
                texto=escolha+","+nome
                s.send(texto)
                print "Aceitando a conexao..."
                if (escolha =="2"):
                        while True:
                            d=s.recv(1024)

                            break;

                        da=d.split(',')
                        print "recebendo hostis"
                        arq = open('Hostis.txt','wb')
                        for i in da:
                            arq.write(i)
                        arq.close()


                if ( escolha == "3"):
                    # con, addr = s.accept()
                    arq = open('arquivuns.mp3','wr') #abrindo o arquivo para escrever o dado recebido

                    while True:
                            d=s.recv(1024)
                            if d== "NE":
                                    print "O Host nao tem esse Arquivo"
                                    break
                            da=d.split(',')
                            #dado = base64.b64decode(d)
                            #print dado
                            arq.write(d)
                            #print d
                            if not d:
                                    break
                    print "gravando no arquivo"
                    arq.close()
                s.close()


        def enviar_arquivo(self,conn, nome):
                print "abrindo arquivo..."
                arq= open(nome,'rb')
                for i in arq.readlines():
                        #dado=base64.b64encode(i)
                        #print dado
                        conn.send(i)
                print "saindo..."
                arq.close()
                print "fechou"


        def lista_arq(self):
                arquivos = []   # pegando lista de arquivos mp3
                arquivos= glob.glob('*.mp3')
                #arquivos.append(glob.glob('*.txt'))

                return  arquivos
