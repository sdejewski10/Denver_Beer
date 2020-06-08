import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

import pandas as pd

session = HTMLSession()
resp = session.get('https://www.grandmasbeer.co/ontap')

resp.html.render()

#print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')


###G ETS ALL BEER INFO - ONLY NAME AND STYLE ON WEBSITE ###
beer = soup.find_all(class_='image-slide-title')

beer_list = []
for b in beer:
    results = (b.text)
    beer_list.append(results)

#print(beer_list) #PRINTS TEXT OF BEER NAME - STYLE

edit_list = beer_list.copy()

### SPLITS BY THE '-' CHARACTER AND RETURNS FIRST ITEM (BEER NAME) ###
beer_name = [i.split('-')[0] for i in edit_list]
#print(beer_name)

### SPLITS BY THE '-' CHARACTER AND RETURNS SECOND ITEM (BEER STYLE) ###
beer_style = [i.split('-')[1] for i in edit_list]
#print(beer_style)

grandma_df = pd.DataFrame({'Brewery':'Grandmas House','Beer':beer_name,'Style':beer_style})
#print(grandma_df)

grandma_df.to_csv('Grandmas.csv',index = False, header= True)
