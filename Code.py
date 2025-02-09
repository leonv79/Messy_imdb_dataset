import pandas as pd
import os
from datetime import datetime
import numpy as np

os.chdir('D:\Documents\KAGGLE\MESSY_DATASET_IMDB')
df = pd.read_excel('messy_IMDB_dataset.xlsx')
df.head()
df.dropna()
df.columns

#Drop the NA Column
df = df.drop('Unnamed: 8',axis=1)
#drop the na rows 
df = df.dropna(how='all')

#rename columns
df.rename(columns={'Original titlΚ':'Original title','Genrλ¨':'Genre'},inplace=True)



#Fix the release dates
df['Release year'].unique()


false_values = []
isinstance(df['Release year'].iloc[0], datetime)
for i in range(0,len(df['Release year'])):
    if isinstance(df['Release year'].iloc[i], datetime)==False:
        value = df['Release year'].iloc[i]
        false_values.append(value)
    
        
    

map = {'09 21 1972':'1972-09-21 00:00:00',' 23 -07-2008':'2008-07-23 00:00:00','22 Feb 04':'2004-02-22 00:00:00','10-29-99':'1999-10-29 00:00:00','23rd December of 1966 ':'1966-11-23 00:00:00','01/16-03':'2003-01-16 00:00:00','The 6th of marzo, year 1951':'1951-03-06 00:00:00',
       '1984-02-34':'1984-03-31 00:00:00','1976-13-24':'1976-03-31 00:00:00',
       '09 21 1972':'1972-03-31 00:00:00'
      }

df['Release year'] = df['Release year'].replace(map,regex=False)
df['Release year'].unique()
df['Release year'] = pd.to_datetime(df['Release year']).dt.year



isinstance(df['Duration'].iloc[4], object)
df['Duration'] = pd.to_numeric(df['Duration'],errors='coerce')



import numpy as np

# Replace infinite values with NaN
df['Duration'] = df['Duration'].replace([np.inf, -np.inf], np.nan)

# Fill NaN with the mean (excluding NaNs)
df['Duration'] = df['Duration'].fillna(df['Duration'].mean())


df['Country'].unique()

#Fix Country names
df['Country'] = df['Country'].apply(lambda x: 'New Zealand' if x == 'New Zesland' or x == 'New Zeland' else x)
df['Country'] = df['Country'].replace('Italy1','Italy')


#Content Ratings
df['Content Rating'].unique()
df['Content Rating'] = df['Content Rating'].replace('Not Rated','Unrated')
df['Content Rating'] = df['Content Rating'].replace(np.nan,'Unrated')
df['Content Rating'] = df['Content Rating'].replace('Approved','G')

#Fix income value errors
df.columns
df['Income'] = df['Income'].str.replace('$','')
df['Income'] = df['Income'].str.replace(',','')
df['Income'] = df['Income'].str.replace('o','0')

df['Income'] = pd.to_numeric(df['Income'])





df[' Votes '] = df[' Votes '].apply(lambda x:int(x))  


df['Score'] = df['Score'].str.replace(',.','.')
df['Score'] = df['Score'].str.replace('..','.')
df['Score'] = df['Score'].str.replace(r'[^0-9]', '',regex=True)



df['Score'] = df['Score'].replace([np.inf, -np.inf], np.nan)

df['Score'] = pd.to_numeric(df['Score'])

df['Score'] = df['Score'].apply(lambda x: x / 10 if x > 100 else (x * 10 if x < 10 else x))


df['Score'] = df['Score'].apply(lambda x:float(x)) 
df['Score'] = df['Score']/10
# Fill NaN with the mean (excluding NaNs)
df['Score'] = df['Score'].fillna(df['Score'].mean())
