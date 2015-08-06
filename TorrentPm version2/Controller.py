__author__ = 'Pedro Cardoso'
from Servidor import Servidor
from Cliente import Cliente
import xml.etree.ElementTree as ET #sql = ET

class Controller():

    def __init__(self):
        print "Menu\n" #falta pedir lista de hosts
        print "[1]Procurar arquivo na minha lista de amigos"
        print "[2] Receber listas de amigos  "
        print "[3]receber arquivo"
        escolha=raw_input()
        if "1" == escolha:
            nome =raw_input("Diga o nome do arquivo")
            c = Cliente()

            #for e in s.lista_clientes:
            c.enviar(nome)
        if "3" ==escolha:
            s = Servidor()


Controller()

#separar esses metodos nas classes de cliente e servidor. 
#não sei mais quem faz o que :'(

def getHosts(): #pede lista de hosts
    root = ET.Element('p2pse')
    gethosts = ET.SubElement(root,'getHosts')

    arq = ET.ElementTree(root)
    ET.dump(root)
    arq.write('getHosts.xml')

def getHostsResponse(ip,port): #responde com a lista dos hosts
    root = ET.Element('p2pse')
    gethostsresponse = ET.SubElement(root,'getHostsResponse')
    host = ET.SubElement(gethostsResponse,'host')
    ip2 = ET.SubElement(host,'ip')
    port2 = ET.SubElement(host,'port')

    #fazer um for aqui  !!!!!!!!!PENSAR!!!!!!!!!!
    #ver como pega ip e porta da conexão
    #lembrar se precisa ser da rede toda ou só das conexões que o server já fez
    ip2.text = ip
    port2 = port

    arq = ET.ElementTree(root)
    ET.dump(root)
    arq.write('getHostsResponse.xml')

def searchFiles(keywords): #manda procurar o arquivo de acordo com as palavras chaves, precisa de leitura pra saber quais as palavras
    root = ET.Element('p2pse')
    searchfiles = ET.SubElement(root,'searchFiles')
    keywords2 = ET.SubElement(root,'keywords')

    keywords2.text = keywords

    arq = ET.ElementTree(root)
    ET.dump(root)
    arq.write('searchFiles.xml')

def searchFilesResponse(file, fileName, fileSize): #devolve o arquivo que foi pedido
    root = ET.Element('p2pse')
    searchfileresponse = ET.SubElement(root,'searchFilesResponse')
    file2 = ET.SubElement(gethostsResponse,'file')
    fileName2 = ET.SubElement(file2,'fileName')
    fileSize2 = ET.SubElement(file2,'fileSize')

    file2.text = file
    fileName2.text = fileName
    fileSize2.text = fileSize

    arq = ET.ElementTree(root)
    ET.dump(root)
    arq.write('getHostsResponse.xml')

def getFiles(fileName): #dá o nome do arquivo pra receber o mesmo
    root = ET.Element('p2pse')
    getFiles = ET.SubElement(root,'getFiles')
    fileName2 = ET.SubElement(getFiles, 'fileName')

    fileName2.text = fileName

    arq = ET.ElementTree(root)
    ET.dump(root)
    arq.write('getFiles.xml')

def getFilesResponse(fileData, fileName, data): #devolve o arquivo
    root = ET.Element('p2pse')
    getFilesResponse = ET.SubElement(root,'getFilesResponse')
    fileData2 = ET.SubElement(getFilesResponse,'fileData')
    fileName2 = ET.SubElement(fileData2,'fileName')
    data2 = ET.Element(fileData2,'data')

    fileData2.text = fileData
    fileName2.text = fileName
    data2.text = data

    arq = ET.ElementTree(root)
    ET.dump(root)
    arq.write('getHostsResponse.xml')
