#GOING TO BE USED TO CONCATENATE ALL THE SEPERATE SCRAPERS INTO ONE LARGE DATA FRAME
import pandas as pd
import glob
import os

### CODE TO RETRIEVE ALL OF THE FILES STORED IN THAT FOLDER ####
path = '/Users/steve/Documents/Coding/Beer_Data/Beer Data'  #PUT ALL THE INDIVIDUAL SCRAPER CSV INTO THIS FILE
files = []
for r, d, f in os.walk(path):
    for file in f:
        if 'csv' in file:
            files.append(os.path.join(r, file))


####prints out each file name individually###
#for f in files:
    #print(f)

### PRINTS LIST OF THE FILES IN THE FOLDER ABOVE ###
#print(files)

#Denver_Beer = pd.concat(files)

#print(Denver_Beer)
