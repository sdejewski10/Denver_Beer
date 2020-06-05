#GOING TO BE USED TO CONCATENATE ALL THE SEPERATE 
# SCRAPERS INTO ONE LARGE DATA FRAME
import pandas as pd
import os

### CODE TO RETRIEVE ALL OF THE FILES STORED IN THAT FOLDER ####
path = '/Users/steve/Documents/Coding/Beer_Data/Beer Data'  #PUT ALL THE INDIVIDUAL SCRAPER CSV INTO THIS FILE
files = []
for r, d, f in os.walk(path):
    for file in f:
        if 'csv' in file:
            files.append(os.path.join(r, file))


### Creating a list of readable DF's and adding to li
li=[]
for f in files:
    df=pd.read_csv(f,index_col=None,header=0)
    li.append(df)


### PRINTS LIST OF THE FILES IN THE FOLDER ABOVE ###
#print(files)

Denver_Beer = pd.concat(li,axis=0,ignore_index=True)

print(Denver_Beer)
