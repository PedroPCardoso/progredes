#!/usr/bin/env python
#coding: utf8
import os, cgi
from datetime import datetime

form = cgi.FieldStorage()

nome = form["nome"].value
comentario = form["coment"].value
data = datetime.now()

savingComents(nome,comentario,data)
htmlOut()


'''def takeDate()
	today = datetime.now()
	day = today.day
	month = today.month
	year = today.year'''

def htmlOut():
	arquivo = open('coments.txt', 'r') #abrindo o arquivo pra leitura
	allComents = arquivo.readlines()

	print "Content-type: text/html; charset=utf-8"
	print
	print "<html><head><title>Comentários</title></head><body>"
	# for x in xrange(1,10):
	print allComents + "<br>"
	print "</body></html>"

def savingComents(nome, comentario, data):
	arquivo = open('coments.txt', 'r') #abrindo o arquivo pra leitura
	texto = arquivo.readlines() #lê o arquivo todo pra pegar a ultima linha e add numa list
	texto.append('Nome:' + nome)  #adiciona o nome do novo coment
	texto.append('Data:' + data)  #adiciona a data do novo coment
	texto.append('Comentário:' + comentario)  #adiciona o coment do novo coment
	texto.append('\n')
	arquivo = open('coments.txt', 'w') # abre o arquivo pra escrita e adiciona a list com o novo coment
	arquivo.writelines(texto) 
	arquivo.close()
	return arquivo














