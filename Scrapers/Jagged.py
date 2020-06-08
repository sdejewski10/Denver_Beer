#INCOMPLETE
import pyppdf.patch_pyppeteer
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

###GETS BEER NAME AND STYLE###

beer_names_list = []
for div in beer_names[0:]:
    results = (div.text)
    beer_names_list.append(results)


###CLEANSING LIST####
beer_names_list.pop(0)

beer_names_list.remove('Get ‘em before they’re gone!')
beer_names_list.remove('More adventurous and creative beers')
beer_names_list.remove('Our most adventurous beers!')
beer_names_list.pop(10)

###BEER STYLE IS EVERY OTHER ELEMENT IN THE LIST###
###STARTING FROM POSITION 1 (THE FIRST BEER STYLE) RETURN EVERY OTHER ELEMENT###
beer_style_list = beer_names_list[1::2]

#print(beer_style_list)

###BEER NAMES ARE EVERY OTHER ELEMENT IN THE LIST###
###STARTING WITH POSITION 0 (THE FIRST BEER NAME) RETURN EVERY OTHER ELEMENT###
beer_names_list = beer_names_list[::2]

#print(beer_names_list)


beer_info = beer_names = soup.find_all('p',style='text-align:center;white-space:pre-wrap;')
#print(beer_info)

beer_info_list = []
for b in beer_info[0:]:
    results = (b.text)
    beer_info_list.append(results)

###CREATING COPY OF LIST TO FILTER/EDIT###
edit_list = beer_info_list.copy()

### REMOVING BLANK RESULTS FROM LIST####
edit_list = [x for x in edit_list if x != '']
edit_list = [x for x in edit_list if x != ' ']

#print(edit_list)

###FILTERING LIST TO RETURN ONLY VALUES THAT CONTAIN ABV###
edit_list = list(filter(lambda x: 'ABV' in x, edit_list ))

###****WHEN USING FILTER IT RETURNS AN ITERATOR, HAVE TO CAST IT USING LIST BEFORE IT####
#print(list(edit_list))

###SPLITTING THOSE VALUES ON THE . AT THE END OF THE DESCRIPTION###
###SHOULD RETURN TWO SEPERATE VALUES FOR EACH BEER, ONE OF DESCRIPTION
### AND ONE OF ABV | IBU###

beer_abv_list = [i.split('.',1) for i in edit_list]
#print(beer_abv_list)

### Selecting the second element from the list above, beer abv/ibu###
def beer(beer_abv_list):
    return [item[1] for item in beer_abv_list]

beer_abv_list = beer(beer_abv_list)

#print(beer_abv_list)

### WILL RETURN LIST seperating the abv and ibu based on the |###
beer_abv_list = [i.split('|') for i in beer_abv_list]
#print(beer_abv_list)


### CREATING LIST THAT RETURNS ONLY ABV PORTION OF THE LIST####
def beer_abv(beer_abv_list):
    return [item[0] for item in beer_abv_list]

beer_abv2_list = beer_abv(beer_abv_list)
#print(beer_abv2_list)

###MANUALLY ENTERING ABV FOR THOSE THAT HAD TEXT IN THE LIST####
beer_abv2_list.insert(6, '5.5%')
beer_abv2_list.pop(7)
beer_abv2_list.insert(8,'6.5%')
beer_abv2_list.pop(9)
beer_abv2_list.insert(9,'7.5%')
beer_abv2_list.pop(10)
beer_abv2_list.insert(11,'10%')
beer_abv2_list.pop(12)
beer_abv2_list.insert(13,'N/A')

#print(beer_abv2_list)



def beer_ibu(beer_abv_list):
    return [item[1] for item in beer_abv_list]

beer_ibu_list = beer_ibu(beer_abv_list)
#print(beer_ibu_list)

beer_ibu_list.insert(13,'N/A')

jagged_df = pd.DataFrame({'Brewery':'Jagged Mountain Brewing','Beer':beer_names_list,'Style':beer_style_list,'ABV':beer_abv2_list,'IBU':beer_ibu_list})

###REMOVING BOTTLED BEER####
jagged_df = jagged_df.drop([12])
#print(jagged_df)

jagged_df.to_csv('Jagged.csv', index = False, header=True)



