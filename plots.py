import pandas as pd

'''
This script plots all the song metrics by decade. 
'''
features1 = pd.read_csv('features1.csv')
features2 = pd.read_csv('features2.csv')
features3 = pd.read_csv('features3.csv')
features4 = pd.read_csv('features4.csv')
features5 = pd.read_csv('features5.csv')

df = pd.concat([features2, features3, features4, features5])
print(df.head())
df.to_csv('features_all.csv')
