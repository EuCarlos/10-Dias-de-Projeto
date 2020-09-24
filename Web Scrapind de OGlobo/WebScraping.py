from urllib.request import urlopen
import time
from bs4 import BeautifulSoup

news = []
arq = open('noticias.txt', 'a')

time.sleep(5)
url = urlopen('https://oglobo.globo.com/')
html = BeautifulSoup(url.read(), 'html.parser')
s = html.find_all('h1', {"class":"teaser__title teaser__title"})
T = html.find_all('h1', {"class":"teaser__title small-teaser__title teaser__title"})
for tag in s and T:
  titulo = tag.getText()
  if (titulo in news):
    continue
  else:
    news.append('NOTICIA:{}'.format(titulo))
    arq.writelines(news)
arq.close()
