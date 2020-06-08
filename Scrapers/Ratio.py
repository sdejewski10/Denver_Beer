#Complete - couldnt get IBU figured out though

import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

import pandas as pd

session = HTMLSession()
resp = session.get('http://ratiobeerworks.com/#/home')

resp.html.render()

#print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

#print(soup.get_text())

#Getting Beer Names
beers = soup.find_all(class_='title')
#print(beer_names)

beer_name_list = []
for b in beers:
    results = (b.text)
    beer_name_list.append(results)

###REMOVING THE "GLASSWARE" FROM LIST'
beer_name_list = beer_name_list[::2]
#print(beer_name_list)

style = soup.find_all('div', class_ = 'label')

beer_style_list = []
for b in style:
    results = (b.text)
    beer_style_list.append(results)

edit_list = beer_style_list.copy()

beer_style_list =[i.split('\n')[2] for i in edit_list]
beer_abv_list = [i.split('\n')[3] for i in edit_list]

#print(len(beer_style_list))
#print(len(beer_abv_list))

ibu = soup.find_all('div', class_='measure')

beer_ibu_list = []
for b in ibu:
    results = (b.text)
    beer_ibu_list.append(results)


beer_ibu_list = [i.split('\n')[2] for i in beer_ibu_list]

ratio_df = pd.DataFrame({'Brewery':'Ratio Beer Works','Beer':beer_name_list,'Style':beer_style_list,'ABV':beer_abv_list})

ratio_df.to_csv('Ratio.csv',index=False,header=True)