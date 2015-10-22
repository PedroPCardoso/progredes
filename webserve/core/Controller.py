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
import sys
'''
from xml.parsers.xmlproc import xmlproc
from xml.parsers.xmlproc import xmlval
from xml.parsers.xmlproc import xmldtd
'''
class Controller():

    def __init__(self):
        print "Menu\n"
        print "[1] Listar hosts locais "
        print "[2] Listar hosts remotos"
        print "[3] Procurar arquivos remotos"
        print "[4] Procurar arquivos local"

        def inicializar(local,porta):
            print "servidor inicializado"
            s=Servidor(local,porta)


        th=Thread( target=inicializar, args = ( "localhost",57001, ) )
        th.start()



    def meushosts(self):
            return self.listHosts()
            #c = Cliente()
            #for e in s.lista_clientes:
            #c.enviar(nome)
            #  listHosts()  #lê o arquivo local de ip e portas e mostra
    def querohosts(self):
             escolha="2"
             pedido="2"
             #XMLENVIADO=getHosts() #tem que enviar esse xml pro outro pc e receber o xml de resposta
             self.cliente(escolha,pedido)
             print "lista recebida com sucesso"
             return "ola"
             # string_xml(XMLRECEBIDO,3)
    def queroarquivo(self):
            escolha="3"

            opcao = raw_input("Digite Nome do arquivo seguido do seu formato : ")

            #     print "formato deve ser digitado dessa forma: *.mp3"
            keywords = raw_input()
            #self.searchMetywords,opcao)
            self.cliente(escolha,keywords)
            #t = threading.Thread(target=self.cliente, args=(keywords))
            #t.start()
    def meusarquivos(self):

            escolha= "4"
            opcao = raw_input("Deseja procurar por: (1) Nome do arquivo ou (2) Formato do arquivo")
            if opcao == "1":
                print "Digite o nome do arquivo:"
            if opcao == "2":
                print "Digite o formato do arquivo:"
                print "formato deve ser digitado dessa forma: .mp3"
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
        str=""
        for i in arquivo_ips.readlines():
                str+=i + ";"
                print str
        arquivo_ips.close()
        return str




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



    #return  xml_getFiles
'''
def validate_xml(xml_filename, dtd_filename):
        Validate a given XML file with a given external DTD.
        If the XML file is not valid, an exception will be
        printed with an error message.
        dtd = xmldtd.load_dtd(dtd_filename)
        parser = xmlproc.XMLProcessor()
        parser.set_application(xmlval.ValidatingApp(dtd, parser))
        parser.dtd = dtd
        parser.ent = dtd
        parser.parse_resource(xml_filename)

        if __name__ == "__main__":
            xml_filename, dtd_filename = sys.argv[1], sys.argv[2]
            validate_xml(xml_filename, dtd_filename)
        '''
"""

def validate_xml(xml_filename, dtd_filename):
Validate a given XML file with a given external DTD.
       If the XML file is not valid, an exception will be
         printed with an error message.
        dtd = xmldtd.load_dtd(dtd_filename)
        parser = xmlproc.XMLProcessor()
        parser.set_application(xmlval.ValidatingApp(dtd, parser))
        parser.dtd = dtd
        parser.ent = dtd
        parser.parse_resource(xml_filename)

if __name__ == "__main__":
        xml_filename, dtd_filename = sys.argv[1], sys.argv[2]
        validate_xml(xml_filename, dtd_filename)
"""
