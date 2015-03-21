#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

url = "http://www.uefs.br/portal"

meta =urllib.urlopen(url) 
html = urllib.urlopen(url).read() # Lendo a url e passando o html
soup = BeautifulSoup(html)

#print meta.info()
#print soup.find_all('a')

def getTamanho():
	meta = url.info()
	print "Content-Length:", meta.getheaders("Content-Length")[0] # retornando tamanho

titulo = soup.title.text 
#print titulo


def getTitle():
	titulo = soup.title.text 
	titulo = titulo.lower() # Colocando em minusculo
	return titulo


for script in soup(["script", "style"]):
	script.extract()    # Tirando os scripts do html

# Pego todo texto sem os scripts
text = soup.get_text()
# print text 
''' Quebra a linha  e remove os espacos da direita e esquerda, 
a funcao strip que remove esses espaços em branco'''
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk) # pular linha

''' Fazer uma funcao usando o BeautifulSoup como eu posso pedir 
pra ele retornar uma parte do codigo html que tem determinada tag
e apartir do retorno dessa lista a gente faz um for que sai comparando se a nossa palavra 
esta no meio dessas.
  '''
#print text
text.encode('utf-8')
print type(text)


def remover_acentos(txt, codif='utf-8'):
    txt = txt.lower() #colocando em minusculo
    ''' Devolve copia de uma str substituindo os caracteres
       acentuados pelos seus equivalentes não acentuados.  '''
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

 
'''def contagem(lista[]):
	for i in lista[]:
		for j in lista[]:
			if i == j:
				t+=1

	return t

'''






lista=[]
palavra = ""
l = [te.encode('UTF8') for te in text] # Transformando o texto um uma lista de unicode utf8

#print text
for t in l:  #transformando em uma lista de string
				
		x = str(t)

		lista.append(t)


print type (lista[23])	

lista2=[]
palavra=""

for v in range(1,len(lista)): # CRIANDO FUCK LISTA DE PAALVRAS
	z= lista[v]

	if z.isspace():
		lista2.append(palavra)
		palavra=""

	else:
		#print z
		palavra+=z

print lista2


