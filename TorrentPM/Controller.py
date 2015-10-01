#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

__author__ = 'Pedro Cardoso e Manuelle Macedo'
from Servidor import Servidor
from Cliente import Cliente
import xml.etree.ElementTree as ET #sql = ET
import os
import glob
import base64
from threading import Thread

class Controller():

    def __init__(self):
        print "Menu\n"
        print "[1] Listar hosts locais "
        print "[2] Listar hosts remotos"
        print "[3] Procurar arquivos localmente"
        print "[4] Procurar arquivos remotos"

        def inicializar(local,porta):
            print "servidor inicializado"
            s=Servidor(local,porta)


        th=Thread( target=inicializar, args = ( "localhost",57001, ) )
        th.start()

        escolha=raw_input()
        if "1" == escolha:
            self.listHosts()
            #c = Cliente()
            #for e in s.lista_clientes:
            #c.enviar(nome)
          #  listHosts()  #lê o arquivo local de ip e portas e mostra
        if "2" == escolha:
             xml= raw_input("xml")
             #XMLENVIADO=getHosts() #tem que enviar esse xml pro outro pc e receber o xml de resposta
             XMLRECEBIDO=self.cliente(escolha,xml)
             print XMLRECEBIDO
            # string_xml(XMLRECEBIDO,3)



        if "3" == escolha:

            opcao = raw_input("Deseja procurar por: (1) Nome do arquivo seguido do seu formato")
            if opcao == "1":
                print "Digite o nome do arquivo junto com o formato do arquivo:"
            if opcao == "2":
                print "Digite o formato do arquivo:"
                print "formato deve ser digitado dessa forma: *.mp3"
            keywords = raw_input()
            #self.searchMetadadosLocal(keywords,opcao)
            self.cliente(escolha,keywords)
            #t = threading.Thread(target=self.cliente, args=(keywords))
            #t.start()

        if "4" == escolha:
            opcao = raw_input("Deseja procurar por: (1) Nome do arquivo ou (2) Formato do arquivo")
            if opcao == "1":
                print "Digite o nome do arquivo:"
            if opcao == "2":
                print "Digite o formato do arquivo:"
                print "formato deve ser digitado dessa forma: *.mp3"
            keywords = raw_input()
            XMLRECEBIDO=self.searchfiles(keywords) #gera xml pra ser enviada
            string_xml(XMLRECEBIDO,opcao)  #xml que ele recebe do outro host
            fileName = raw_input ("Digite o nome do arquivo se deseja obtê-lo")
            getFiles(fileName) #gera xml pra ser enviada caso ele queira o arquivo
            string_xml(XMLRECEBIDO,opcao) #xml que ele recebe do outro host
    def servidor(self):
        s= Servidor("locaohost",50001)



    def cliente(self, escolha,nome):
        c=Cliente()
        return c.enviar(escolha,nome)
    def listHosts(self):
        arquivo_ips = open('lista_ips.txt', 'r')
        lista_ips = arquivo_ips.readlines()
        for i in lista_ips:
                print (i)
        arquivo_ips.close()



    def string_xml(reading_allXml, opcao): #chega a string xml pra ler e saber o que e
        tree = ET.parse(reading_allXml)
        root = tree.getroot() # recupera a tag principal

        for child in root: # procura os subelements
            if child.tag == ("getHosts"):
                return getHostsResponse() #retorna o xml com a lista de ips e portas ///  transmitir/enviar

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
                return searchMetadados(palavrachave, opcao) #numero da opção se for rocurar pelo nome ou pelo tamanho /// retorna o xml de searchresponde

            if child.tag == ("searchFilesResponse"):
                lista_nome = []
                lista_tamanho = []
                for nome  in root.iter('fileName'):
                    lista_nome.append(nome.attrib) # cria uma lista com todos os nomes
                for tamanho in root.iter('fileSize'):
                    lista_tamanho.append(tamanho.attrib) # cria uma lista com todos os tamanhos


            if child.tag == ("getFiles"):
                palavrachave = root.iter('fileName')
                return getFilesResponse(palavrachave)

            if child.tag == ("getFilesResponse"):
                data = root.iter('data')
                decode_data = decode64(data)
                nome_arquivo = root.iter('fileName')
                arquivo_recebido = open(nome_arquivo, 'w')
                arquivo_recebido.write(decode_data)
                arquivo_recebido.close()

Controller()


#------------------------------------------------------------------------FUNCOES AUXILIARES---------------------------------------------------------------
def savingHosts(ip, port): #quando se conectar a alguem chama essa função
    arquivo = open('/lista_ips_ports.txt','a') #ler o txt antes e jogar no sets
    lista = []
    lista.append (ip + ',' + port + '\n') #ANOTAÇÃO tem que ver se funfa esse barra n
    arquivo.writelines(lista)
    arquivo.close()


#ok
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
def getHosts(): #pede lista de hosts
    root = ET.Element('p2pse')
    gethosts = ET.SubElement(root,'getHosts')

    #xml_gethosts = ET.ElementTree(root)
    xml_gethosts = ET.dump(root)

    return xml_gethosts #tem problema aqui, quando do print aqui aparece none

#OK
def getHostsResponse(): #responde com a lista dos hosts
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

 #   arq = ET.ElementTree(root)
    xml_gethostsresponse = ET.dump(root)

    return xml_gethostsresponse

#OK
def searchFiles(keywords): #manda procurar o arquivo de acordo com as palavras chaves, precisa de leitura pra saber quais as palavras
    root = ET.Element('p2pse')
    searchfiles = ET.SubElement(root,'searchFiles')
    keywords2 = ET.SubElement(root,'keywords')

    keywords2.text = keywords

    #arq = ET.ElementTree(root)
    xml_searchFiles = ET.dump(root)

    return xml_searchFiles

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

   # arq = ET.ElementTree(root)
    xml_searchFilesResponse = ET.dump(root)

    return  xml_searchFilesResponse

def getFiles(fileName): #dá o nome do arquivo pra receber o mesmo
    root = ET.Element('p2pse')
    getFiles = ET.SubElement(root,'getFiles')
    fileName2 = ET.SubElement(getFiles, 'fileName')

    fileName2.text = fileName

    #arq = ET.ElementTree(root)
    xml_getFiles = ET.dump(root)

    return  xml_getFiles

def getFilesResponse(fileName): #devolve o arquivo
    root = ET.Element('p2pse')
    getFilesResponse = ET.SubElement(root,'getFilesResponse')
    fileData2 = ET.SubElement(getFilesResponse,'fileData')
    fileName2 = ET.SubElement(fileData2,'fileName')
    data2 = ET.Element(fileData2,'data')

    fileName2.text = fileName
    data2.text = encode64(fileName)

    #arq = ET.ElementTree(root)
    xml_getFiles = ET.dump(root)

    return  xml_getFiles
