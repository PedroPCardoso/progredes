import socket
import thread

class server:
    HOST = ''              # Endereco IP do Servidor
    PORT = 4000            # Porta que o Servidor esta
    BUFFER_SIZE = 1024

    def _init_(self):
        conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destination = (HOST, PORT)
        conection = blind(destination)
        conection.listen(1) #ver que argumento é esse
        while True: #lembrar o que faz esse while ASHUAH
            con, addressClient = conection.accept()
            thread.start_new_thread(conectado, tuple([con, cliente]))

    
    def recevingMessage(xmlDecode):
        data = con.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        con.send(data)  # echo
        con.close() #num entendi esse con
        
    def conectado(con, cliente):
        print 'Conectado por', cliente

            while True:
                msg = con.recv(1024)
                if not msg: break
                print cliente, msg
                
    def closeConection:
        print 'Finalizando conexao do cliente', cliente
        conection.close()
        thread.exit()


