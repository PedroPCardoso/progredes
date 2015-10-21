# Cliente
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import base64
import glob
from threading import Thread
import xml.etree.ElementTree as ET #sql = ET

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

                if escolha=="2":
                    root = ET.Element('p2pse')
                    gethosts = ET.SubElement(root,'getHosts')

                    xml_gethosts = ET.ElementTree(root)
                    ET.dump(root)

                    xml_gethosts.write('getHosts.xml')
                    self.enviar_arquivo(s,"getHosts.xml")
                    #s.send(texto)
                    print "Aceitando a conexao..."
                    while True:
                        d=s.recv(1024)

                        break;

                    print "recebendo hostis"
                    arq = open('Hostis.xml','wb')
                    for i in d:
                        arq.write(i)
                    arq.close()

                if escolha=="3":

                    root = ET.Element('p2pse')
                    getFiles = ET.SubElement(root,'getFiles')
                    fileName2 = ET.SubElement(getFiles, 'fileName')

                    fileName2.text = nome

                    xml_getFiles = ET.ElementTree(root)
                    ET.dump(root)

                    xml_getFiles.write('getFiles.xml')

                    self.enviar_arquivo(s,"getFiles.xml")
                    #texto=escolha+","+nome

                    #s.send(texto)
                    print "Aceitando a conexao..."
                    while True:
                        d=s.recv(1024)

                        break;

                    print "recebendo hostis"
                    arq = open('Hostis.jpg','wb')

                    for i in d:
                        arq.write(self.decode64(i))
                    arq.close()



        def getHosts(): #pede lista de hosts
            root = ET.Element('p2pse')
            gethosts = ET.SubElement(root,'getHosts')

            xml_gethosts = ET.ElementTree(root)
            ET.dump(root)

            xml_gethosts.write('getHosts.xml')

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
                arquivos= glob.glob('*.jpg')
                #arquivos.append(glob.glob('*.txt'))

                return  arquivos
# paradinhaaas





# Parte de tratamento de dados #


        ''    #ok
        def searchMetadadosLocal(keywords, opcao): #procurando pelo tamanho do arquivo
            list_arqs = []
            j = 0
            if opcao == "1": #nome do arquivo
                list_arqs = os.listdir('C:/Users/Manu/Documents/server') #mudar o caminho para a pasta que quer

            if opcao == "2": #formato do arquivo
                list_arqs = glob.glob(keywords)

            for i in list_arqs:
                if keywords == i:
                    fileSize = os.path.getsize('C:/Users/Manu/Documents/server/' + i) # mudar p caminho para a pasta que quer
                    print (i)
                    print (fileSize)

        def searchMetadados(keywords, opcao): #procurando pelo tamanho do arquivo
            list_arqs = []
            nome_arq = []
            tam_arq = []
            j = 0
            if opcao == "1": #nome do arquivo
                list_arqs = os.listdir('/')
                for i in list_arqs:
                    if keywords == i:
                        fileSize = os.path.getsize('/' + i)
                        nome_arq[j] = i
                        tam_arq[j] = fileSize
                        j=+1
                return searchFilesResponse(nome_arq, tam_arq)


            if opcao == "2": #formato do arquivo
                list_arqs = glob.glob(keywords)
                for i in list_arqs:
                    if keywords == i:
                        fileSize = os.path.getsize('/' + i)
                        nome_arq[j] = i
                        tam_arq[j] = fileSize
                        j=+1
                return searchFilesResponse(nome_arq, tam_arq)


        def encode64(fileName):
            lista_aux = []
            list_arqs = os.listdir('/')
            for i in list_arqs:
                    if fileName == i:
                        arq = open(i,'r+b')
                        for j in arq.readlines():
                            data=+base64.standard_b64encode(j)
                        arq.close()
                        return data

        def decode64(data):
            return base64.standard_b64decode(data)


        #----------------------------------------------------------------------------XML--------------------------------------------------------------------
        #OK


            #return xml_gethosts #tem problema aqui, quando do print aqui aparece none

        #OK
        def getHostsResponse(self): #responde com a lista dos hosts
            root = ET.Element('p2pse')
            gethostsresponse = ET.SubElement(root,'getHostsResponse')
            host = ET.SubElement(gethostsresponse,'host')

            arquivo_ips = open('lista_ips.txt', 'r')
            lista_ips = arquivo_ips.readlines()
            for i in lista_ips:
                    ip = ET.SubElement(host,'ip')
                    port = ET.SubElement(host,'port')
                    i_t = i.split(',')
                    ip.text = i_t[0]
                    port.text = i_t[1]
            arquivo_ips.close()

            xml_gethostsresponse = ET.ElementTree(root)
            ET.dump(root)

            xml_gethostsresponse.write('getHostsResponse.xml')
                    #return xml_gethostsresponse

            #OK
        def searchFiles(keywords): #manda procurar o arquivo de acordo com as palavras chaves, precisa de leitura pra saber quais as palavras
            root = ET.Element('p2pse')
            searchfiles = ET.SubElement(root,'searchFiles')
            keywords2 = ET.SubElement(root,'keywords')

            keywords2.text = keywords

            xml_searchFiles = ET.ElementTree(root)
            ET.dump(root)


            xml_searchFiles.write('searchFiles.xml')
            #return xml_searchFiles

        #pra testar isso aqui preciso testar searchMetadados :O
        def searchFilesResponse(nome_arq, tam_arq): #devolve os dados do arquivo que foi pedido
            root = ET.Element('p2pse')
            searchfileresponse = ET.SubElement(root,'searchFilesResponse')
            file2 = ET.SubElement(searchfileresponse,'file')

            for i in nome_arq: # percorre as linhas da matriz (nome)
                fileName2 = ET.SubElement(file2,'fileName')
                fileName2.text = i
                for j in tam_arq: #percorre as colunas (tamanho)
                    fileSize2 = ET.SubElement(file2,'fileSize')
                    fileSize2.text = j
                    break

            xml_searchFilesResponse = ET.ElementTree(root)
            ET.dump(root)

            xml_searchFilesResponse.write('searchFilesResponse.xml')
            #return  xml_searchFilesResponse

        def getFiles(fileName): #da o nome do arquivo pra receber o mesmo
            root = ET.Element('p2pse')
            getFiles = ET.SubElement(root,'getFiles')
            fileName2 = ET.SubElement(getFiles, 'fileName')

            fileName2.text = fileName

            xml_getFiles = ET.ElementTree(root)
            ET.dump(root)

            xml_getFiles.write('getFiles.xml')
            #return  xml_getFiles







        def string_xml(self,reading_allXml, opcao): #chega a string xml pra ler e saber o que e
            tree = ET.parse(reading_allXml)
            root = tree.getroot() # recupera a tag principal

            for child in root: # procura os subelements
                if child.tag == ("getHosts"):
                    return self.getHostsResponse() #retorna o xml com a lista de ips e portas ///  transmitir/enviar

                if child.tag == ("getHostsResponse"):
                    lista_ips = []
                    lista_ports = []
                    for ips  in root.iter('ip'):
                        lista_ips.append(ips.attrib) # cria uma lista com todos os ips
                    for port in root.iter('port'):
                        lista_ports.append(port.attrib) # cria uma lista com todas as portas

                    tamanho = lista_ips.lenght
                    print "LISTA DE IPS E PORTAS"
                    for i in range(0,(tamanho-1)):
                        print ('IP:', lista_ips[i])
                        print ('PORTA:', lista_ports[i])

                if child.tag == ("searchFiles"):
                    palavrachave = root.iter('keywords')
                    return searchMetadados(palavrachave, opcao)
                if child.tag == ("searchFilesResponse"):
                    lista_nome = []
                    lista_tamanho = []
                    for nome  in root.iter('fileName'):
                        lista_nome.append(nome.attrib) # cria uma lista com todos os nomes
                    for tamanho in root.iter('fileSize'):
                        lista_tamanho.append(tamanho.attrib) # cria uma lista com todos os tamanhos


                if child.tag == ("getFiles"):
                    palavrachave = root.iter('fileName')
                    self.getFilesResponse(palavrachave)

                if child.tag == ("getFilesResponse"):
                    data = root.iter('data')
                    #decode_data = decode64(data)

                    nome_arquivo = root.iter('fileName')
                    arquivo_recebido = open(nome_arquivo, 'w')
                    arquivo_recebido.write(decode_data)
                    arquivo_recebido.close()





        def getFilesResponse(self,fileName): #devolve o arquivo
            root = ET.Element('p2pse')
            getFilesResponse = ET.SubElement(root,'getFilesResponse')
            fileData2 = ET.SubElement(getFilesResponse,'fileData')
            fileName2 = ET.SubElement(fileData2,'fileName')
            data2 = ET.Element(fileData2,'data')
                
            fileName2.text = fileName
            data2.text = encode64(fileName)

            xml_getFilesresponse = ET.ElementTree(root)
            ET.dump(root)

            xml_getFilesresponse.write('getfilesResponse.xml')
