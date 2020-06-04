#INCOMPLETE - left out IBU list because only 8 entries and didnt feel like matching up
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession


from urllib.request import Request, urlopen
import pandas as pd

session = HTMLSession()
resp = session.get('https://www.nextstopbrew.co/in-the-taproom')

resp.html.render()

#print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

#print(soup.get_text())

#Code to get Beer Names
beer_names = soup.find_all('span',class_='item')

#check to see if beer name text is included
#print(beer_names)

#loop for beer names to retrieve text and put results in list form
beer_name_list =[]
for b in beer_names[0:]:
    results = (b.text)
    beer_name_list.append(results)

beers_name_list = beer_name_list[:-2]

#print(beers_name_list)

beer_styles = soup.find_all('span', class_='beer-style')
#print(beer_styles)

beer_style_list = []
for bs in beer_styles[0:]:
    results = (bs.text)
    beer_style_list.append(results)

#print(len(beer_style_list))

#CODE FOR BEER ABV
beer_abv = soup.find_all('span',class_='abv')

beer_abv_list=[]
for b in beer_abv[0:]:
    results = (b.text)
    beer_abv_list.append(results)

#print(len(beer_abv_list))

#CODE FOR BEER IBU
beer_ibu = soup.find_all('span',class_='ibu')

beer_ibu_list=[]
for b in beer_ibu[0:]:
    results = (b.text)
    beer_ibu_list.append(results)

#print(beer_ibu_list)

NS_df = pd.DataFrame({'Brewery':'Next Stop','Beer':beer_name_list,'Style':beer_style_list,
'ABV':beer_abv_list,})
print(NS_df)