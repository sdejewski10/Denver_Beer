#complete

#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd

#Rendering webpage in case javascript##
session = HTMLSession()
resp = session.get('http://www.baerebrewing.com/beers.html')

resp.html.render()

#print(resp)

#MAKING THE SOUP
soup = BeautifulSoup(resp.html.html, features='lxml')

### GETTING BEER NAMES ###
beers = soup.select('.beer-name > a ')
beer_list = []
for b in beers:
    results = (b.text)
    beer_list.append(results)

edit_list = [i.split('\n') for i in beer_list]
def cleanse(edit_list):
    return [item[1] for item in edit_list]

beer_list = cleanse(edit_list)

print(beer_list)

### GETTING STYLE ###
style_list = []
def style():
    style = soup.find_all(class_='beer-style')
    for s in style:
        style_results = (s.text)
        style_list.append(style_results)

style()
print(style_list)

abv_list = []
def abv():
    abv = soup.find_all(class_='abv')
    for a in abv:
        abv_results = (a.text)
        abv_list.append(abv_results)

abv()
print(abv_list)

Baere_df = pd.DataFrame({'Brewery':'Baere','Beer':beer_list,'Style':style_list,'ABV':abv_list,'IBU':'N/A'})
Baere_df.to_csv('Baere.csv', index = False, header = True)