#INCOMPLETE CANT GET BEER STYLE
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession


from urllib.request import Request, urlopen
import pandas as pd

session = HTMLSession()
resp = session.get('https://www.trvebrewing.com/ontap')

resp.html.render()

#print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

#print(soup.get_text())

#Code to get Beer Names
beer_names = soup.find_all('strong')

#check to see if beer name text is included
#print(beer_names)

#loop for beer names to retrieve text and put results in list form
beer_name_list =[]
for b in beer_names[0:]:
    results = (b.text)
    beer_name_list.append(results)

#print(beer_name_list)

beer_styles = soup.find_all('p')
#print(beer_styles)

beer_style_list = []
for bs in beer_styles[0:]:
    results = (bs.text)
    beer_style_list.append(results)

print(beer_style_list)