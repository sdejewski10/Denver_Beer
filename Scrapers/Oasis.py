#COMPLETE

import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession


from urllib.request import Request, urlopen
import pandas as pd

session = HTMLSession()
resp = session.get('https://www.oasisbeer.com/beer-menu')

resp.html.render()

#print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

### GETTING BEERS###

beers = soup.find_all(class_='font_8')


beer_list = []
for b in beers:
    results = (b.text)
    beer_list.append(results)

beer_names = beer_list[0:5]

#print(beer_names)
beer_names.pop(1)
beer_names.pop(2)
#print(beer_names)

add_beer_names = soup.find_all(class_='font_2')
add_names_list = []
for b in add_beer_names:
    results = (b.text)
    add_names_list.append(results)

edit_list = add_names_list.copy()
add_names_list = [i.split(',') for i in edit_list]


def added_beer(add_names_list):
    return [item[0] for item in add_names_list]

beer_list = (added_beer(add_names_list))


##REMOVING RANDOM ELEMENT####
beer_list.remove('\u200b')

### BEER NAMES ARE EVERY SECOND ELEMENT####
beer_list = beer_list[0::2]
beer_list.pop(9) #REMOVING OASIS BREWERY FROM BEER LIST
#print(beer_list)

styles = []
for s in soup.select('.font_2 > span'):
    results = (s.text)
    styles.append(results)

styles.remove('\u200b')

beer_abv_list = styles[1::2]
#print(beer_style_list)

beer_abv_edit = beer_abv_list.copy()

beer_edit_list = beer_abv_list.copy()

#SPLITS ON BLANK SPACES & RETURNS SEPERATE ELEMENTS LIKE: %, ABV, #, IBU
beer_abv_list = [i.split() for i in beer_abv_edit]
beer_edit_list = [i.split() for i in beer_abv_edit]
#print(beer_style_list)

#JOINGING THE FIRST TWO VALUES OF EACH LIST SO IT RETURNS: % ABV
def merges(lst):
    for b in lst:
        b[0:2] = [' '.join(b[0:2])]

#RUNNING LIST ABOVE THROUGH FUNCTION CREATED TO MERGE VALUES
merges(beer_abv_list)

### ABOVE STILL RETURNS LIST OF LIST, SELECTING ONLY ABV
def abv(beer_abv_list):
    return [item[0] for item in beer_abv_list]

beer_abv_list = abv(beer_abv_list)
#print(beer_abv_list)


### GETTING IBU ###
def ibu_merge(lst):
    for x in lst:
        x[1:2] = [''.join(x[1:2])]

def ibus(lst):
    return [item[3] for item in beer_edit_list]

ibu_list = ibus(beer_edit_list)
#print(len(ibu_list))

oasis_df = pd.DataFrame({'Brewery':'Oasis Brewing','Beer':beer_list,'Style':'N/A','ABV':beer_abv_list,'IBU':ibu_list})
oasis_df.to_csv('Oasis.csv', index = False, header = True)