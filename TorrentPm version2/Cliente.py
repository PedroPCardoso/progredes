# Cliente
import socket
import base64
import glob
class Cliente:

        def __init__(self):
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                print "conectando com servidor..."
                #s.connect((HOST,PORT))
                #self.enviar(s)

        def enviar(self,nome):
                HOST='localhost' #coloca o host do servidor
                PORT=57001


                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                print "conectando com servidor..."
                s.connect((HOST,PORT))
                texto="1"+ ","+nome

                s.send(texto)

        def enviar_arquivo(self,s, nome):
                print "abrindo arquivo..."
                arq=open(nome,'rb')

                print "enviado  arquivo"
                for i in arq.readlines():
                        #print i
                        #dado=base64.standard_b64encode(i)
                        s.send(i)

                print "saindo..."
                arq.close()

        def lista_arq(self):
                arquivos = []   # pegando lista de arquivos mp3
                arquivos= glob.glob('*.mp3')
                #arquivos.append(glob.glob('*.txt'))

                return  arquivos
