import socket
import base64

class client:
    HOST = '10.65.102.96'     # Endereco IP do Servidor
    PORT = 4000            # Porta que o Servidor esta
    BUFFER_SIZE = 1024
    
    def _init_(self):
        conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destination = (HOST, PORT)
        conection.connect(destination)
        print 'Conexão Aberta!\n'

    def sendMessage(xmlEncode):
        conection.send(xmlEncode)
        print 'Mensagem Enviada!'
        print xmlEncode

    def closeConection():
        tcp.close()

    def encode(xml):
        file_encoded = base64.b64encode(xml) # ver como vai ser com arquivo

    def 
