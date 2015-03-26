#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
from unicodedata import normalize


url = "http://www.uefs.br/portal"
#url = str (raw_input("digite o site : ex: http://www.facebook.com      "))
meta =urllib.urlopen(url) 
html = urllib.urlopen(url).read() # Lendo a url e passando o html
soup = BeautifulSoup(html)

for script in soup(["script", "style"]):
	script.extract()    # Tirando os scripts do html
# Pego todo texto sem os scripts
text = soup.get_text()
#print text 
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
esta no meio dessas.'''
#print text
text.encode('utf-8')
#metodo retorna informaçoes adicionais sobre o site


def informacoes(): 
	print meta.info()
#print soup.find_all('a')


def getTamanho():
	meta2 = meta.info()
	print "###### Tamanho da Pagina em Bytes:########", meta2.getheaders("Content-Length")[0] # retornando tamanho

titulo = soup.title.text 
def getTitle():
	titulo = soup.title.text 
	titulo = titulo.lower() # Colocando em minusculo
	print titulo
	return titulo

print "################ Titulo e Informaçoes: ###########################"
informacoes()
getTamanho()
getTitle()
# funcao que remove os acentos de palavras
def remover_acentos(txt, codif='utf-8'):
    txt = txt.lower() #colocando em minusculo
    ''' Devolve copia de uma str substituindo os caracteres
       acentuados pelos seus equivalentes não acentuados.  '''
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')



def List_Palavras(text):
	lista=[]
	palavra = ""
	l = [te.encode('UTF8') for te in text] # Transformando o texto um uma lista de unicode utf8
	for t in l:  #transformando em uma lista de string
				
			x = str(t)

			lista.append(t)
	lista2=[]
	palavra=""

	for v in range(0,len(lista)): # CRIANDO FUCK LISTA DE PAALAVRAS
		z= lista[v]

		if z.isspace():
			lista2.append(palavra)
			palavra=""

		else:
		#print z
			palavra+=z
	return lista2
# print lista2 caso queira printa a lista de todas as palavras
def contas_Palavras(lista2): #conta as palavras distintas
	lista3=[]
	quant=0 # Funcao contar as palavras
	for v in range(1,len(lista2)):
		for t in range(2,len(lista2)):
			if lista2[v] == lista2[t]:
				quant += 1
	print quant
print"############################ Quantidade de Palavras distintas contidas no html ########################################"
lista2 =List_Palavras(text)
contas_Palavras(lista2)
def getCentroide(soup,text):
	tagList =[]
	pesos =[]
	tags = open ('pesos.txt', 'r')
	for x in range(1,21):
		p = tags.readline()
		z= p.split()
		pesos.append(int(z[1]))
		tagList.append(z[0])
	l = List_Palavras(text)
	dic =[]
	vezs=0
	pontos=0
	stop = open ('stoplist.txt', 'r')
	for i in l:
		for x in stop.readline():
			if i == x:
				l.remove(i)
				
	'''stop2 = open ('stoplistEN.txt', 'r')
	for i in l:
		for x in stop.readline():
			if i == x:
				l.remove(i)
	'''
	for palavra in l:
		i=0
		for tag in tagList:
			z = soup.find_all(tag)
			t = str(z)
			g = t.split(palavra)
			vezs += (len(g) -1 )
			pontos += pesos[i]*(len(g) - 1)
			i+=1
		dic.append(palavra)
		dic.append(pontos)
		dic.append(vezs)
		pontos=0
		vezs =0
	print dic
	#print dic.items()
print "################################# CENTROIDE (Palavra,Pontos e Vezes que aparece)################################"
getCentroide(soup,text)
#Funcao que printa todas as palavras sem o acento
def sema_cento() : 
	lista2 = List_Palavras(text)
	lista_semacent=[]
	for i in lista2: # asdiciona as palavras sem acento dentro de uma nova lista
		lista_semacent.append(remover_acentos(i))
	print lista_semacent

print"############################# PALAVRAS SEM ACENTOS ###################################################"
sema_cento()
	