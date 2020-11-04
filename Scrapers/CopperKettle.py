###COMPLETE###

#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import selenium
from selenium import webdriver

url = 'https://www.copperkettledenver.com/beer'
#Rendering webpage in case javascript##

dirty_names_list = []
names_list = []
style_list = []
abv_list = []
ibu_list = []


def scraping():
    browser = webdriver.Chrome()
    browser.get(url)

    beer_names = browser.find_elements_by_css_selector(
        'h4 > span:nth-child(2)')
    for b in beer_names[:-1]:
        name = (b.text.strip())
        print(name)
        names_list.append(name)

    abvs = browser.find_elements_by_class_name(
        "font_7")
    for a in abvs:
        info = (a.text)
        print(info)
        style_list.append(info)

    for i in style_list:
        splits = i.split('/')
        abv = splits[0]
        abv_list.append(abv)

    print(len(abv_list))
    print(len(names_list))

    new_abv_list = abv_list[7:18]
    print(new_abv_list)
    print(len(new_abv_list))

    path_to_save = '/Users/steve/Documents/Coding/Beer_Data/Beer Data/CSV Files/'
    df = pd.DataFrame({"Brewery": "Copper Kettle", "Beer": names_list,
                       "Style": '', "ABV": new_abv_list, "IBU": ''})
    df.to_csv(path_to_save+'CopperKettle.csv', index=False, header=True)


scraping()
