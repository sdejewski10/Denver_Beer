#COMPLETE

import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

import pandas as pd

session = HTMLSession()
resp = session.get('https://greatdivide.com/beers/')

resp.html.render()

print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

#print(soup.get_text())

#Getting Beer Names
beer_names = soup.find_all('h5',class_='portfolio-title')
print(len(beer_names))

beer_names_list = []
for x in beer_names[0:]:
    results = (x.text)
    beer_names_list.append(results)

#print(beer_names_list)

beer_style = soup.find_all('h6',class_='portfolio-subtitle')

beer_style_list = []
for x in beer_style[0:]:
    results = (x.text)
    beer_style_list.append(results)

print(len(beer_style_list))

GD_df = pd.DataFrame({'Brewery':'Great Divide Brewing Co','Beer':beer_names_list,'Style':beer_style_list})
print(GD_df)

GD_df.to_csv('Great_Divide.csv',index= False, header= True)
