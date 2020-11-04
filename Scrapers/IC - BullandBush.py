### CANT GET ABV####

#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd

url = 'https://bullandbush.com/pages/menu#beermenu'
#Rendering webpage in case javascript##

dirty_names_list = []
names_list = []
style_list = []
abv_list = []
ibu_list = []


def scraping():
    session = HTMLSession()
    resp = session.get(url)
    resp.html.render()
    soup = BeautifulSoup(resp.html.html, features='lxml')

    table_rows = soup.find_all('tr')
    for t in table_rows[1:29]:
        beer = t.find('h5')
        names = beer.get_text()
        names_list.append(names)
        styles = t.find('br').next_sibling
        print(styles)
        style_list.append(styles)
        br = styles.next_sibling
        print(type(br))
        # abv = br.next_sibling


scraping()
