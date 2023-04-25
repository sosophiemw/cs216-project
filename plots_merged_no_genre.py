import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast
import datetime
import numpy as np
from scipy import stats

merged_df = pd.read_csv('merged_data.csv')
date_df = merged_df[['date']]
feat_df = merged_df[['features']]


feat_df = feat_df['features'].astype('str')
feat_df = feat_df.apply(lambda x: ast.literal_eval(x))
feat_df = feat_df.apply(pd.Series)
#print(feat_df)

df = date_df.join(feat_df)
df = df[['date','energy','danceability', 'speechiness', 'acousticness', 'tempo']]
df["year"]= df["date"].apply(lambda x: datetime.date.fromisoformat(x).year)
#print(df['year'])

df = df[['year','energy','danceability', 'speechiness', 'acousticness', 'tempo']]
df1 = df[(df['year'] >= 1970) & (df['year'] <= 1980)]
df2 = df[df['year'] >= 2001]

df_old = df1.groupby(['year']).mean()
df_new = df2.groupby(['year']).mean()
print(df_old)
print(df_new)

'''
Statistical Testing
'''
n_old = len(df_old.index) 
n_new = len(df_new.index)

mean_old_energy = np.mean(df_old['tempo'])
mean_new_energy = np.mean(df_new['tempo'])
std_old_energy = np.std(df_old['tempo'])
std_new_energy = np.std(df_new['tempo'])
answer_energy = stats.ttest_ind_from_stats(mean_old_energy, std_old_energy, n_old,
                                                 mean_new_energy, std_new_energy, n_new)
print(answer_energy)
'''
Plotting section
'''
#sns.relplot(df_grouped, x='year', y='energy').set(title='Average Energy Level of Top 15 Songs per Year')
#sns.relplot(df_grouped, x='year', y='danceability').set(title='Average Danceability of Top 15 Songs per Year')
#sns.relplot(df_grouped, x='year', y='speechiness').set(title='Average Speechiness of Top 15 Songs per Year')
#sns.relplot(df_grouped, x='year', y='acousticness').set(title='Average Acousticness of Top 15 Songs per Year')
#sns.relplot(df_grouped, x='year', y='tempo').set(title='Average Tempo of Top 15 Songs per Year')
plt.show()