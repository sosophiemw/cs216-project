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
df.to_csv('features_all.csv')

first = pd.read_csv('first.csv')
second = pd.read_csv('second.csv')
third = pd.read_csv('third.csv')
fourth = pd.read_csv('fourth.csv')
fifth = pd.read_csv('fifth.csv')
sixth = pd.read_csv('sixth.csv')

df2 = pd.concat([first, second, third, fourth])
df2.to_csv('first-sixth_all.csv')

df_merged = df2.merge(df, how='inner', left_on='track_uri', right_on='uri')
df_merged.to_csv('merged_data.csv')

genres1 = pd.read_csv('genres1.csv')
genres2 = pd.read_csv('genres2.csv')
genres3 = pd.read_csv('genres3.csv')
genres4 = pd.read_csv('genres4.csv')
genres5 = pd.read_csv('genres5.csv')

df3 = pd.concat([genres1, genres2, genres3, genres4, genres5])
df3.to_csv('genres_all.csv')

df_merged = df3.merge(df_merged, how='inner', on = 'uri')
df_merged.to_csv('merged_data.csv')
print(df_merged)
