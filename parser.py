#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
from unicodedata import normalize


lista=[""]
url = urllib.urlopen("http://www.uefs.br") 
meta = url.info()
print "Content-Length:", meta.getheaders("Content-Length")[0]
#print html_completo
html = BeautifulSoup(url)
print "titulo: "
print html.title.text
titulo = html.title.text 
titulo = titulo.lower() # Colocando em minusculo
print titulo
lista_palavras = titulo.split()
lista_palavras.append("açao") # So pra testar se funfava ;3
print lista_palavras


def getTitle():
	return titulo
 
def remover_acentos(txt, codif='utf-8'):
    txt = txt.lower() #colocando em minusculo
    ''' Devolve copia de uma str substituindo os caracteres
       acentuados pelos seus equivalentes não acentuados.  '''
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

for i in lista_palavras: # adiciona as palavras sem acento dentro de uma nova lista
	lista.append(remover_acentos(i))
print lista


for a in html.find_all('a', attrs = {'span': 'class'}):
	print a.text
url.close()
