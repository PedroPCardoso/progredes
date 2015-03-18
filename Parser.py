import urllib
from bs4 import BeautifulSoup

url = "http://www.uefs.br/portal"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

titulo = soup.title.text 
print titulo

def getTitle():
	titulo = soup.title.text 
	titulo = titulo.lower() # Colocando em minusculo
	return titulo

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()
# print text 
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk) # pular linha

#print text
print type(text)

