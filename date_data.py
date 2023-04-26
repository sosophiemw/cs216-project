#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:12:12 2023

@author: mcpenguin
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:04:01 2023

@author: mcpenguin
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:11:12 2023

@author: mcpenguin
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:21:54 2023

@author: mcpenguin
"""


import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re


#plt.style.use("seaborn-whitegrid")
#plt.rc("figure", autolayout=True)
#plt.rc("axes", labelweight="bold", labelsize="large", titleweight="bold", titlesize=14, titlepad=10)

df = pd.read_csv('billboarddata.csv')

jan_date = re.compile(r'([0-9]+-01)')
df["Data"]  = df["date"].str.extract(jan_date)
df=df.dropna()


################ Music Brainz  Data
import requests
import musicbrainzngs as mbz 
# https://musicbrainz.org/doc/MusicBrainz_API
# https://musicbrainz.org/doc/MusicBrainz_API/Examples
# https://realpython.com/api-integration-in-python/


#https://python-musicbrainzngs.readthedocs.io/en/latest/api/

# REST API data access 
api_url = 'https://musicbrainz.org/ws/2/'

req1 = 'https://musicbrainz.org/ws/2/area/45f07934-675a-46d6-a577-6f8637a411b1?inc=aliases'
req2 = 'https://musicbrainz.org/ws/2/artist/all?fmt=json'
req3 = 'https://musicbrainz.org/ws/2/area/db325bd7-ae64-40bd-966a-a3af3cef8bb9?fmt=json'
req4 = api_url + 'area?query=california&fmt=json'
req5 = api_url + 'artist'

response = requests.get(req4)


#Python bindings
app = "RecordIndustry.io"
version = "0.1"
mbz.set_useragent(app, version, contact=None)




#may be better if this is a dictionary: alas... it is not

def get_placedata(name_artist, begin_area_list, country_list):
    string=name_artist
    result=mbz.search_artists(query=string, limit=None, offset=None, strict=True)
    try: 
        artist=result['artist-list'][0]
        #print(artist)
    except: 
        artist="N/A"
    try:
        begin_area=(artist['begin-area']["name"])
    except:
        begin_area="N/A"
    try:
         country=(artist['country'])
    except:
         country="N/A"
    country_list.append(country)
    begin_area_list.append(begin_area)
    return begin_area_list, country_list


country_list=[]
begin_area_list=[]
artist_list=[]


for artist in df["artist"]:
    print(artist)
    begin_area_list, country_list=get_placedata(artist, begin_area_list, country_list)
    
    #get_countrylist[artist, country_list]



# PUT These Back into Dat_Frame From Above

#May want to spot check that nothing weirdly got out of order
#If anyone wants to get fancy...
# may be better to make a dataframe based on the artist, and then merge these frames together, rather than code below

df["country"]=country_list
df["city"]=begin_area_list



####GRAPHING:
#Look, a GRAPH!
#country_counts=df.groupby("country")["Artists"].count().reset_index(name ="counts")
#country_counts=country_counts.sort_values("counts", ascending=False)
#sns.barplot(data=country_counts, x="country", y="counts", color="blue")


df.to_csv('date_data.csv', index=False) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
