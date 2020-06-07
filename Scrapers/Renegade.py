#COMPLETE
import pyppdf.patch_pyppeteer
import requests
from bs4 import BeautifulSoup

from urllib.request import Request, urlopen
import pandas as pd

req = Request('https://renegadebrewing.com/our-beers/',headers={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()

#MAKING THE SOUP

soup = BeautifulSoup(webpage, features='lxml')

#Getting Beer Names
beer_names = soup.find_all(class_='title-heading-center')

beer_name_list =[]
for b in beer_names[0:]:
    results = (b.text)
    beer_name_list.append(results)

#print(beer_name_list)

#Some heading text included in the above beer list, reomving and create new list with only
#beer names

b = 2
beer_names_list = beer_name_list[b:-9]

#print(beer_names_list)

#Getting Beer Style
beer_style = soup.find_all(class_='sub-t-beer')

beer_style_list =[]
for b in beer_style[0:-9]:
    results = (b.text)
    beer_style_list.append(results)

#print(beer_style_list)

#Getting BeER ABV

beer_abv = soup.find_all(class_='percentage')

beer_abv_list=[]
for b in beer_abv[0:-9]:
    results = (b.text)
    beer_abv_list.append(results)

#print(beer_abv_list)

#GETTING BEER IBU

beer_ibu = soup.find_all(class_='ibu')

beer_ibu_list = []
for b in beer_ibu[0:-9]:
    results = (b.text)
    beer_ibu_list.append(results)

#print(beer_ibu_list)

#CREATING DATAFRAME

Renegade_df = pd.DataFrame({'Brewery':'Renegade Brewing','Beer':beer_names_list,'Style':beer_style_list,
'ABV':beer_abv_list,'IBU':beer_ibu_list})
print(Renegade_df)

Renegade_df.to_csv('Renegade.csv',index=False,header=True)
