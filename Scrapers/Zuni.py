#Incomplete - need to get beer styles figured out

import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession


from urllib.request import Request, urlopen
import pandas as pd

session = HTMLSession()
resp = session.get('https://www.zunistreet.com/beers-listed')

resp.html.render()

#print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

#print(soup.get_text())

#Getting Beer Names
beer_names = soup.find_all('strong')
#print(beer_names)

beer_name_list =[]
for b in beer_names[0:]:
    results = (b.text)
    beer_name_list.append(results)

#print(beer_name_list)

edit_list = beer_name_list.copy()
#print('copied')
edit_list = edit_list[:-1]
#print(edit_list)

#Splitting by comma and returning the first element(The beer name)

new_beer_list = [i.split(',') for i in edit_list]
#print(new_beer_list)

#removing hour from beer list
beer_name_list = [i.split(',')[0] for i in edit_list]
#print(beer_name_list)

beer_abv_list = [i.split(',')[1] for i in edit_list]
#print(beer_abv_list)

beer_ibu_list = [i.split(',')[2] for i in edit_list]

#print(beer_ibu_list)

beer_style = soup.find_all('div', class_='sqs-block-content')
#print(beer_style)

beer_style_list =[]
for b in beer_style[0:]:
    results = (b.text)
    beer_style_list.append(results)

print(beer_style_list)

#beer_styles = [i.split('/') for i in beer_style_list]
#print(beer_styles)


