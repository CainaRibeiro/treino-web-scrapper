#Biblioteca para pegar informações de uma URL
#O python é capaz de ler apenas o único arquivo que você requisitou


from urllib.request import urlopen

#Ler https://docs.python.org/3/library/urllib.html, documento sobre a biblioteca urllib

#Instalando a biblioteca BeautifulSoup
#Usaremos a biblioteca BeautifulSoup 4 ou BS4

#from bs4 import BeautifulSoup em um terminal python

from bs4 import BeautifulSoup

html = urlopen('https://guilhermemuller.com.br/ead/html-css-na-pratica/pagina-html-basica')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.header)