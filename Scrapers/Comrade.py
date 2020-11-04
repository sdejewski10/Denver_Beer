#FILE SETUP#
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd

url = 'https://comradebrewing.com/brews/'
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

    names = soup.find_all(class_='beer-name')
    for n in names:
        name = (n.text)
        print(name)
        dirty_names_list.append(name)

    abvs = soup.find_all(class_='abv')
    for a in abvs:
        abv = (a.text)
        abv_list.append(abv)

    ibu_location = []
    ibu_index = soup.find_all(class_='beer')
    for num, i in enumerate(ibu_index):
        # print(num)
        try:
            location = i.find(class_='ibu').get_text()
            # print(location)
            ibu_list.append(location)
        except:
            ibu_list.append('')

    # print(len(dirty_names_list))

    # print(dirty_names_list)
    for d in dirty_names_list:
        splits = d.split('\n')
        print(splits)
        names_list.append(splits[2])
        style_list.append(splits[4])

    print(len(abv_list))
    print(len(ibu_list))
    print(len(names_list))
    print(len(style_list))

    path_to_save = '/Users/steve/Documents/Coding/Beer_Data/Beer Data/CSV Files/'

    df = pd.DataFrame({'Brewery': 'Comrade Brewing', 'Beer': names_list,
                       'Style': style_list, 'ABV': abv_list, 'IBU': ibu_list})
    df.to_csv(path_to_save+'Comrade.csv', index=False, header=True)


scraping()
