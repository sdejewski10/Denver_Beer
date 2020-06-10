#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd

#Rendering webpage in case javascript##
session = HTMLSession()
resp = session.get('http://www.blackprojectbeer.com/current-draft-list')

resp.html.render()

#print(resp)

#MAKING THE SOUP
soup = BeautifulSoup(resp.html.html, features='lxml')

### GETTING BEER NAMES ###
beers = soup.find_all(class_='item')

beer_list = []
for b in beers:
    results = (b.text)
    beer_list.append(results)

#print(beer_list)

### GETTING BEER STYLE ###
style = soup.find_all(class_='item-title-color item-bg-color item-info padding-left')
beer_style_list = []
for b in style:
    results = (b.text)
    beer_style_list.append(results)

#print(beer_style_list)

edit_list = beer_style_list.copy()

edit_list_v2 = [i.split('\n') for i in edit_list]
