import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast
import datetime

merged_df = pd.read_csv('merged_data.csv')
date_df = merged_df[['date']]
genre_df = merged_df[['genres']]
feat_df = merged_df[['features']]


feat_df = feat_df['features'].astype('str')
feat_df = feat_df.apply(lambda x: ast.literal_eval(x))
feat_df = feat_df.apply(pd.Series)
#print(feat_df)

df = date_df.join(feat_df)
df = df.join(genre_df)
df_energy = df[['date','energy','danceability', 'speechiness', 'acousticness', 'tempo', 'genres']]
df_energy["year"]= df_energy["date"].apply(lambda x: datetime.date.fromisoformat(x).year)
df_energy['year'] = df_energy['date'].str.slice(0,4)
df_grouped = df_energy[['year','energy','danceability', 'speechiness', 'acousticness', 'tempo']]
df_grouped = df_grouped.groupby(['year']).mean()
df_grouped = df_grouped.reset_index()
df_grouped = df_grouped.rename(columns={'index': 'year'})
print(df_grouped)

df_genres = df_energy[['year', 'energy','danceability', 'speechiness', 'acousticness', 'tempo', 'genres']]
df_genres_top5 = df_genres[(df_genres['genres'] == 'album rock') |
                           (df_genres['genres'] == 'dance pop') |
                           (df_genres['genres'] == 'contemporary r&b') |
                           (df_genres['genres'] == 'adult standards') |
                           (df_genres['genres'] == 'classic soul')]
print(df_genres_top5)

#ax = sns.lineplot(data = df_grouped, x='year', y='energy')
#ax = sns.lineplot(data = df_grouped, x='year', y='danceability')
#ax = sns.lineplot(data = df_grouped, x='year', y='speechiness')
#ax = sns.lineplot(data = df_grouped, x='year', y='acousticness')
#ax = sns.lineplot(data = df_grouped, x='year', y='tempo')

#ax = sns.lineplot(data = df_genres_top5, x='year', y='energy', hues = 'genres')
#ax = sns.lineplot(data = df_genres_top5, x='year', y='danceability', hues = 'genres')
#ax = sns.lineplot(data = df_genres_top5, x='year', y='speechiness', hues = 'genres')
#ax = sns.lineplot(data = df_genres_top5, x='year', y='acousticness', hues = 'genres')
ax = sns.lineplot(data = df_genres_top5, x='year', y='tempo', hue = 'genres', ci = False)

for ind, label in enumerate(ax.get_xticklabels()):
    if ind % 5 == 0:  # every 5th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.show()