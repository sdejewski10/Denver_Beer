#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import selenium
from selenium import webdriver

url = 'https://www.copperkettledenver.com/beer'

dirty_names_list = []
names_list = []
style_list = []
abv_list = []
ibu_list = []


def scraper():
    browser = webdriver.Chrome()
    browser.get(url)
    cssselector = '#menu-57974 > div:nth-child({}) > div.section-items-container > div.item-bg-color.menu-items-container.padding-left.padding-right > div:nth-child(1) > div > div.beer-details.item-title-color > p > a'
    for i in range(15):
        cssselector.format(i)
        try:
            names = browser.find_elements_by_css_selector(cssselector)
