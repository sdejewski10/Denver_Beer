#COMPLETE

import requests
from bs4 import BeautifulSoup

from urllib.request import Request, urlopen
import pandas as pd

req = Request('https://www.odellbrewing.com/beer/',headers={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()

#MAKING THE SOUP

soup = BeautifulSoup(webpage, features='lxml')

#Getting Beer Names
beer_names = soup.find_all(class_='beers__title')
#print(beer_names)

beer_name_list =[]
for b in beer_names[0:]:
    results = (b.text)
    beer_name_list.append(results)

#print(beer_name_list)

beer_style = soup.find_all(class_='beers__type')

beer_style_list=[]
for b in beer_style[0:]:
    results = (b.text)
    beer_style_list.append(results)

beer_style_list.pop(0)
#print(beer_style_list)

#print(len(beer_style_list))

beer_abv = soup.find_all(class_='beers__abv')

beer_abv_list=[]
for b in beer_abv[0:]:
    results = (b.text)
    beer_abv_list.append(results)

#print(len(beer_abv_list))

Odell_df = pd.DataFrame({'Brewery':'Odell Brewing Co','Beer':beer_name_list,'Style':beer_style_list,'ABV':beer_abv_list})
print(Odell_df)