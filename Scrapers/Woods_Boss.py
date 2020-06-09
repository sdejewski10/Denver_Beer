#COMPLETE

import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
from requests_html import HTMLSession

import pandas as pd

session = HTMLSession()
resp = session.get('https://www.woodsbossbrewing.com/beers')

resp.html.render()

#print(resp)

#MAKING THE SOUP
soup = BeautifulSoup(resp.html.html, features='lxml')


beer_names = soup.find_all('div', class_ = 'beer')
beer_name_list = []
for b in beer_names:
    results = (b.text)
    beer_name_list.append(results)

#print(beer_name_list)

edit_list = beer_name_list.copy()
beer_name_list = [i.split('\n') for i in edit_list]
#print(beer_name_list)

def beer_names_func(beer_name_list):
    return [item [10] for item in beer_name_list]

beer_title = beer_names_func(beer_name_list)
#print(beer_title)

#print(beer_names_func(beer_name_list)
    

def beer_abv(beer_name_list):
    return [item[17] for item in beer_name_list]

beer_abv_list = (beer_abv(beer_name_list))
#print(beer_abv_list)
beer_abv_list.insert(29,'0')
beer_abv_list.pop(30)
beer_abv_list.insert(31,'0')
beer_abv_list.pop(32)
beer_abv_list.insert(32,'0')
beer_abv_list.pop(33)
#print(beer_abv_list)

beers = soup.find_all('span', class_ ='item-title-color')
beer_style = []
for b in beers:
    results = (b.text)
    beer_style.append(results)

beer_style = [i.split("-")[0] for i in beer_style]

#print(len(beer_style))

wb_df = pd.DataFrame({'Brewery':'Woods Boss Brewing Co','Beer':beer_title,'Style':beer_style, 'ABV':beer_abv_list
})

#print(wb_df)

wb_df.to_csv('Woods_Boss.csv', index = False, header= True)