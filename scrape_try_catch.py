#!/usr/local/opt/python/libexec/bin/python

"""  Scraping Websites with Python3 """

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1 ) 

    print(bs.html.body.h1)
    print(bs.body.h1)
    print(bs.html.h1)
