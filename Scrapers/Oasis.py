##INCOMPLETE - BEER NAMES NOT IN SAME ELEMT ON WEBSITE

import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession


from urllib.request import Request, urlopen
import pandas as pd

session = HTMLSession()
resp = session.get('https://www.oasisbeer.com/beer-menu')

resp.html.render()

#print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

### GETTING BEERS###

beers = soup.find_all(class_='font_8')


beer_list = []
for b in beers:
    results = (b.text)
    beer_list.append(results)

beer_names = beer_list[0:5]

#print(beer_names)
beer_names.pop(1)
beer_names.pop(2)
#print(beer_names)

add_beer_names = soup.find_all(class_='font_2')
add_names_list = []
for b in add_beer_names:
    results = (b.text)
    add_names_list.append(results)

edit_list = add_names_list.copy()
add_names_list = [i.split(',') for i in edit_list]


def added_beer(add_names_list):
    return [item[0] for item in add_names_list]

print(added_beer(add_names_list))


