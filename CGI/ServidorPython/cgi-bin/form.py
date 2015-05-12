#!/usr/bin/env python
#coding: utf8
import os, cgi
from datetime import datetime

form = cgi.FieldStorage()

def savingComents
	

def takeDate
	today = datetime.now()
	day = today.day
	month = today.month
	year = today.year

#acho que tem que fazer um for pra mostrar todos
def htmlOut
	print "Content-type: text/html; charset=utf-8"
	print
	print "<html><head><title>Post Example</title></head><body>"
	print "Nome: "+ form["nome"].value + "<br>"
	print "Data: "+ today + "<br>"
	print "Comentário: "+ form["sexo"].value + "<br>"
	print "</body></html>"
