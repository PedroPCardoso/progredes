#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
from bs4 import BeautifulSoup
from unicodedata import normalize


url = "http://www.shutterstock.com/cat.mhtml?autocomplete_id=&language=pt&lang=pt&search_source=&safesearch=1&version=llv1&searchterm=bike&media_type=images&page=1"
url2= " http://www.rgbstock.com/images/bike"

url3 ="http://www.stockvault.net/search/?query=bike"



def lista_urls(url):
    html = urllib2.urlopen(url).read() # Lendo a url e passando o html

    soup = BeautifulSoup(html)

    print soup.find_al

    i=0
    for url in soup.find_all("img"):
	i+=1
	urllib.urlretrieve(url.get('src'),"foto"+str(i)+ ".jpg")
        print " vai vai vai vai vai "

lista_urls(url)
