#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 13:58:32 2023

@author: mcpenguin
"""

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('country_data.csv')



#Showing plot of the most common countries that artists are from:
country_counts=df.groupby("country")["Artists"].count().reset_index(name ="counts")
country_counts=country_counts.sort_values("counts", ascending=False)
#sns.barplot(data=country_counts, x="country", y="counts", color="blue")




#Showing plot of the most common
country=df.groupby("Country")["country"].count()
gkk = df.groupby(['Country', 'country'])

#US_plot=

#sns.barplot(data=country_counts, x="country", y="counts", color="blue")

print(df.head())
print(country_counts.head())