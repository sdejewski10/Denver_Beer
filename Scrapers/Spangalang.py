#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd

#Rendering webpage in case javascript##
url = ('https://spangalang-brewery.myshopify.com/collections/to-go-beer')
session = HTMLSession()
resp = session.get(url)

resp.html.render()

#print(resp)

#MAKING THE SOUP
soup = BeautifulSoup(resp.html.html, features='lxml')