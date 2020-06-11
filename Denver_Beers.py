#GOING TO BE USED TO CONCATENATE ALL THE SEPERATE 
# SCRAPERS INTO ONE LARGE DATA FRAME
import pandas as pd
import numpy as np 
import sqlalchemy
import sqlite3
import os
import psycopg2

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

#print(Denver_Beer)

#Denver_Beer.to_csv('Denver_Beer.csv', index= False)

### CREATING SQL DATABASE CONNECTION ####

###Importing library that allows POSTGRESQL####
from sqlalchemy import create_engine

###Engine = 'type of sql://username:password@host_name/database_name####
engine = create_engine('postgresql://steve:steve@localhost/beer_db')


### WRITING PANDAS DATAFRAME TO SQL####

## CONNECTING TO POSTGRESQL & DATABASE ##
con = engine.connect()

##DATAFRAME.TO_SQL('TABLE NAME OR VARIABLE CONTAINING TABLENAME', CONNECTION)
table_name = 'beer_info'
Denver_Beer.to_sql(table_name,con)
#print(engine.table_names())
con.close()