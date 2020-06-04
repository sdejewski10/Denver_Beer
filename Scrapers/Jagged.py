#INCOMPLETE

from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession


from urllib.request import Request, urlopen
import pandas as pd

session = HTMLSession()
resp = session.get('https://www.jaggedmountainbrewery.com/beer')

resp.html.render()

print(resp)

#MAKING THE SOUP

soup = BeautifulSoup(resp.html.html, features='lxml')

beer_names = soup.find_all('h3')
#print(beer_names)

beer_names_list = []
for div in beer_names[0:]:
    results = (div.text)
    beer_names_list.append(results)

print(beer_names_list)
