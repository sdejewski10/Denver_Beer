#COMPLETE
import pyppdf.patch_pyppeteer
import requests
from bs4 import BeautifulSoup

import urllib.request
import pandas as pd

url = urllib.request.urlopen('https://denverbeerco.com/on-tap-today/').read()

#MAKING THE SOUP

soup = BeautifulSoup(url, features='lxml')

#BELOW PULLS ALL BEER NAMES WITH HTML TAGS, WHEN INSPECTING SITE, ALL BEERS HAVE H4 TAG PRIOR

#beers = soup.find_all('h4')
#print(beers)

#loops through the information above and searches the H4 tags for text with the
# es-title class


#Returns all the beer names with HTML Code
beer_names = soup.find_all('h4', class_='es-title')


#Defining the variable to store a list of the beer names
#Loops through each and removes the HTML code and adds it to the list
beer_name_list = []
for div in beer_names[0:]:
            result = (div.text)
            beer_name_list.append(result)

#removes the three non-alc drinks from the list
beer_name_list = beer_name_list[:-3]

#print(beer_name_list)


#Creates data frame 
DBC_df = pd.DataFrame({'Brewery':'Denver Beer Co','Beer':beer_name_list,'Style':
['Porter','IPA','Hazy IPA','IPA','Lager','Kolsch','Sour','Sour','Lager','Pale Ale','Blonde Ale','IPA','Seltzer','Seltzer','Seltzer','Seltzer']})
print(DBC_df)




