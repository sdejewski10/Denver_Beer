#COMPLETE
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

import pandas as pd

session = HTMLSession()
resp = session.get('https://www.blackshirtbrewingco.com/taplist')

resp.html.render()

print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

#print(soup.get_text())

#Getting Beer Names
beer_names = soup.find_all('h3')
#print(beer_names)

#Returns a ton of non needed info
beer_name_list =[]
for b in beer_names[0:]:
    results = (b.text)
    beer_name_list.append(results)

#print(beer_name_list)

#Copying list to try a few different theories to return only beer names
edit_list = beer_name_list.copy()
#print('List Copied')

#Removing easy values that i kow arent beer names located at first and last values of list
edit_list.pop(0)
edit_list = edit_list[:-1]
#print(edit_list)

#Now i have list of only beer names, style, abv seperated by '|'
#USE BELOW TO SPLIT LIST BASED ON CERTAIN CHARACTER
all_beer_list = [i.split('|',2)[0] for i in edit_list]

#print(all_beer_list)

beer_style_list =[i.split('|',2)[1] for i in edit_list]

#print(beer_style_list)

beer_abv_list = [i.split('|',2)[2] for i in edit_list]

#print(beer_abv_list)

Black_Shirt_df = pd.DataFrame({'Brewery':'Black Shirt Brewing Co','Beer':all_beer_list,'Style':beer_style_list,
'ABV':beer_abv_list})
print(Black_Shirt_df)


#extracting the lists within the lists created above into their seperate lists
#all beer list provides all the information for each beer, need to convert them into
#beer name list, beer style list, and beer abv list

#def name_of_beer(all_beer_list):
    #return[item[0]for item in all_beer_list]
    
#print(name_of_beer(all_beer_list))

#beer_name_list = name_of_beer(all_beer_list)
#print(beer_name_list)

#extracting style of beer
#def style_of_beer(all_beer_list):
    #return[item[1] for item in all_beer_list]

#beer_style_list = style_of_beer(all_beer_list)
#print(beer_style_list)
