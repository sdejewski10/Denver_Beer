
#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd

#Rendering webpage in case javascript##
session = HTMLSession()
resp = session.get('https://www.14erbrewing.com/beermenu')

resp.html.render()

#print(resp)

#MAKING THE SOUP
soup = BeautifulSoup(resp.html.html, features='lxml')

beers = soup.find_all('p',class_='beer-name')

beer_list = []
for b in beers[0:]: #for every element in beers
    results = (b.text) #every element in beers is turned to text
    beer_list.append(results) #take the text stored in results variable and add to beer list

#print(beer_list) #prints with alot of /n tags and includes beer style, need to split and cleanse

###CREATING LIST TO EDIT AND CLEANSE###
edit_list = beer_list.copy()

beer_names = [i.split('\n') for i in edit_list] #splits on the new line

###REMOVING BLANKS FROM RESULTS OF FIRST SPLIT####
beer_names = [x for x in beer_names if x != '']
#print(beer_names)

def beer_style(beer_names):
    return [item[4] for item in beer_names]

beer_style_list = beer_style(beer_names)
#print(len(beer_style_list))

###Returning the third result from above (beer names)
def beer_name_list(beer_names):
    return [item[2] for item in beer_names]

beer_names = beer_name_list(beer_names)
#print(len(beer_names))

### GETTING ABV ###

beer_abv = soup.find_all(class_='abv')

beer_abv_list = []
for b in beer_abv[0:]:
    results = (b.text)
    beer_abv_list.append(results)

#print(len(beer_abv_list))

### GETTING IBU ###
beer_ibu = soup.find_all(class_='ibu')

beer_ibu_list = []
for b in beer_ibu[0:]:
    results = (b.text)
    beer_ibu_list.append(results)


#IBU ONLY HAS 41 RESULTS - need to organize and get to 53
#print(len(beer_ibu_list))

fourteen_df = pd.DataFrame({'Brewery':'14er Brewing','Beer':beer_names,'Style':beer_style_list,'ABV':beer_abv_list})
#print(fourteen_df)

fourteen_df.to_csv('14er.csv', index = False, header= True)



