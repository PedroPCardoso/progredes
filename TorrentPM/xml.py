#!/usr/bin/python
# coding:utf-8
import xml.etree.ElementTree as ET #sql = ET

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
