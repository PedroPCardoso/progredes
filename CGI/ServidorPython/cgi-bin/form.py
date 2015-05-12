#!/usr/bin/env python
#coding: utf8
import os, cgi
from datetime import datetime

form = cgi.FieldStorage()

nome = form["nome"].value
comentario = form["coment"].value
data = datetime.now()

arquivo = open('coments.txt', 'r') #abrindo o arquivo pra leitura
texto = arquivo.readlines() #lê o arquivo todo pra pegar a ultima linha e add numa list
texto.append('Nome:' + nome + '\n')  #adiciona o nome do novo coment
texto.append('Data:' + str(data) + '\n')  #adiciona a data do novo coment
texto.append('Comentário:' + comentario + '\n')  #adiciona o coment do novo coment
#texto.append('\n') # pra detereminar o fim de um coment
arquivo = open('coments.txt', 'w') # abre o arquivo pra escrita e adiciona a list com o novo coment
arquivo.writelines(texto) 
arquivo.close()

arquivo2 = open('coments.txt', 'r') #abrindo o arquivo pra leitura
allComents = arquivo2.readlines() # lê todas as linhas do arquivo e coloca em uma lista e cada linha é uma posição da lista

print "Content-type: text/html; charset=utf-8"
print
print "<html><head><title>Comentários</title></head><body>"
for x in xrange(0,len(allComents)):
	print str(allComents[x]) + "<br>" + '\n' # tem que ler todas as linhas 
print "</body></html>"
