#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd

url = 'https://www.fourbulletsbrewery.com/'
#Rendering webpage in case javascript##

names_list = []
info_list = []


def scraping():
    session = HTMLSession()
    resp = session.get(url)
    resp.html.render()
    soup = BeautifulSoup(resp.html.html, features='lxml')

    names = soup.find_all(class_='font_4')
    for n in names:
        name = (n.text)
        print(name)
        names_list.append(name)

    infos = soup.find_all(class_='font_8')
    for i in infos:
        info = (i.text)
        print(info)
        info_list.append(info)

    print(len(names_list))
    print(len(info_list))


scraping()
