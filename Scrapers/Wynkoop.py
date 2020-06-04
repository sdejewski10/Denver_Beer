#COMPLETE

#new computer requires this patch because it sends requests to quickly
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession


from urllib.request import Request, urlopen
import pandas as pd

session = HTMLSession()
resp = session.get('https://wynkoop.com/brewery/tap-list/')

resp.html.render()

print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

#print(soup.get_text())

#Getting Beer Names
beer_names = soup.find_all('p', class_='beer-name')
#print(beer_names)

beer_name_list =[]
for b in beer_names[0:]:
    results = (b.text)
    beer_name_list.append(results)

#print(beer_name_list)

edit_list = beer_name_list.copy()
#print('copied')

#Splitting by the new line and returning the third value(The beer name)
all_beer_list = [i.split('\n')[2] for i in edit_list]
#print(all_beer_list)

beer_style_list = [i.split('\n')[4] for i in edit_list]
#print(beer_style_list)

#GETTING BEER ABV
beer_abv = soup.find_all('span', class_='abv')
#print(beer_abv)

beer_abv_list =[]
for b in beer_abv[0:]:
    results = (b.text)
    beer_abv_list.append(results)

#print(beer_abv_list)


#GETTING BEER IBU
beer_ibu = soup.find_all('span', class_='ibu')
#print(beer_ibu)

beer_ibu_list =[]
for b in beer_ibu[0:]:
    results = (b.text)
    beer_ibu_list.append(results)

#print(beer_ibu_list)

Wynkoop_df = pd.DataFrame({'Brewery':'Wynkoop','Beer':all_beer_list,'Style':beer_style_list,
'ABV':beer_abv_list,'IBU':beer_ibu_list})
#print(Wynkoop_df)

path_out = '/Users/steve/Documents/Coding/Beer_Data/Beer_Data/CSV_Files'
Wynkoop_df.to_csv('Wynkoop Data',index=False,header=True)