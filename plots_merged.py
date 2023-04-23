import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast
import datetime

merged_df = pd.read_csv('merged_data.csv')
date_df = merged_df[['date']]
feat_df = merged_df[['features']]


feat_df = feat_df['features'].astype('str')
feat_df = feat_df.apply(lambda x: ast.literal_eval(x))
feat_df = feat_df.apply(pd.Series)
#print(feat_df)

df = date_df.join(feat_df)
df_energy = df[['date','energy','danceability', 'speechiness', 'acousticness', 'tempo']]
#df_energy["year"]= df_energy["date"].apply(lambda x: datetime.date.fromisoformat(x).year)
df_energy['year'] = df_energy['date'].str.slice(0,4)
df_grouped = df_energy[['year','energy','danceability', 'speechiness', 'acousticness', 'tempo']]
df_grouped['year'] = df_grouped['year'].astype(int)
df_grouped = df_grouped[df_grouped['year'] >= 1970]
df_grouped = df_grouped.groupby(['year']).mean()

sns.lineplot(df_grouped, x='year', y='energy')
#sns.lineplot(df_grouped, x='year', y='danceability')
#sns.lineplot(df_grouped, x='year', y='speechiness')
#sns.lineplot(df_grouped, x='year', y='acousticness')
#sns.lineplot(df_grouped, x='year', y='tempo')
plt.show()