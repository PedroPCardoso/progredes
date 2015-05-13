#!/usr/bin/python
# coding:utf-8
import xml.etree.ElementTree as ET #sql = ET

def getHosts():
	root = ET.Element('p2pse')
	gethosts = ET.SubElement(root,'getHosts')
	arq = ET.ElementTree(root)
	ET.dump(root)
	arq.write('getHosts.xml')

def getHostsResponse():
	root = ET.Element('p2pse')
	gethostsresponse = ET.SubElement(root,'getHostsResponse')
	host = ET.SubElement(gethostsResponse,'host')
	ip2 = ET.SubElement(host,'ip')
	port2 = ET.Element(host,'port')

	arq - ET.ElementTree(root)
	ET.dump(root)
	arq.write('getHostsResponse.xml')

def searchFiles():
	root = ET.Element('p2pse')
	searchfiles = ET.SubElement(root,'searchFiles')
	keywords = ET.SubElement(root,'keywords')
	arq = ET.ElementTree(root)
	ET.dump(root)
	arq.write('searchFiles.xml')

def searchFilesResponse():
	root = ET.Element('p2pse')
	searchfileresponse = ET.SubElement(root,'searchFilesResponse')
	file2 = ET.SubElement(gethostsResponse,file1)
	 = ET.SubElement(host,ip)
	port = ET.Element(host,port)

	arq = ET.ElementTree(root)
	ET.dump(root)
	arq.write('getHostsResponse.xml')

def getFiles():
	root = ET.Element('p2pse')
	gethosts = ET.SubElement(root,'getFiles')
	arq = ET.ElementTree(root)
	ET.dump(root)
	arq.write('getFiles.xml')

def getFilesResponse():
	root = ET.Element('p2pse')
	gethostsResponse = ET.SubElement(root,'getFilesResponse')
	host = ET.SubElement(gethostsResponse,'host')
	ip = ET.SubElement(host,ip)
	port = ET.Element(host,port)

	arq = ET.ElementTree(root)
	ET.dump(root)
	arq.write('getHostsResponse.xml')

'''
#escrita
root = ET.Element('pycursos') #no pai
gtk = ET.SubElement(root, 'pyGTK') #n filho 
django = ET.SubElement(gtk, 'Django') #no filho, do filho
django.text = 'Django matando o PHP!' 
arq = ET.ElementTree(root)

ET.dump(root) #constroi o arquivo

#arq.write('pycursos_final.xml')

#leitura
doc = ET.parse('pycursos.xml')

root = doc.getroot() # recupera a tag principal

print root.tag, root.attrib['nome'] # dicionario

#listar a galera
for i in root:
	print i.tag, i.attrib['nome']
	
for i in root.iter('cidade'):
	print i.tag, i.attrib['nome']
'''