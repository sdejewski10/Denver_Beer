#COMPLETE
import pyppdf.patch_pyppeteer
import requests
from bs4 import BeautifulSoup

from urllib.request import Request, urlopen
import pandas as pd

req = Request('https://prostbrewing.com/biers/',headers={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()

#Got denied by security using simple method
#url = urllib.request.urlopen('https://prostbrewing.com/biers/').read()

#MAKING THE SOUP

soup = BeautifulSoup(webpage, features='lxml')

beer_names = soup.find_all('h2',class_='headline black xxspace lined')
#print(beer_names)

beer_names_list = []
for div in beer_names[0:]:
    results = (div.text)
    beer_names_list.append(results)

#print(beer_names_list)

beer_styles = soup.find_all('div', class_='beer-style gold xbold xspace upper')
#print(beer_styles)

beer_style_list = []
for bs in beer_styles[0:]:
    results = (bs.text)
    beer_style_list.append(results)

#print(beer_style_list)

#getting ABV and IBU info from site
beer_info = soup.find_all('ul', class_='beer-info clean ilb xbold xspace upper')
#print(beer_info)

#when above is printed, the ABV and IBU are together, trying to seperate below

beer_abv_list =[]
for b in beer_info[0:]:
    bi_result = (b.text)[5:8]
    beer_abv_list.append(bi_result)

beer_abv_list.insert(11,0)

#print(beer_abv_list)

beer_ibu_list = []
for b in beer_info[0:]:
    results = (b.text)[9:]
    beer_ibu_list.append(results)

beer_ibu_list.insert(11,0)

#print(beer_ibu_list)


Prost_df = pd.DataFrame({'Brewery':'Prost Brewing Co','Beer':beer_names_list ,'Style':beer_style_list,
'ABV':beer_abv_list,'IBU':beer_ibu_list})
#print(Prost_df)

Prost_df.to_csv('Prost.csv', index= False, header= True)
