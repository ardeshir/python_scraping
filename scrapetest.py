#!/usr/local/opt/python/libexec/bin/python

"""  Scraping Websites with Python3 """

from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")

print("Python3 Scraping")
print(" ") 

print( html.read() ) 
