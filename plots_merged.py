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
df_grouped['year'] = pd.to_numeric(df_grouped['year'])
df_grouped = df_grouped[df_grouped['year'] >= 1970]
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
df_genres_top5['year'] = df_genres_top5['year'].astype(int)
print(df_genres_top5)

# ax = sns.lineplot(data = df_grouped, x='year', y='energy')
# ax = sns.lineplot(data = df_grouped, x='year', y='danceability')
# ax = sns.lineplot(data = df_grouped, x='year', y='speechiness')
# ax = sns.lineplot(data = df_grouped, x='year', y='acousticness')
# ax = sns.lineplot(data = df_grouped, x='year', y='tempo')

#ax = sns.relplot(data = df_genres_top5, x = 'year', y = 'energy', col = 'genres', ci = False, kind = 'line',
#                hue = 'genres', height = 3)
#ax = sns.relplot(data = df_genres_top5, x = 'year', y = 'danceability', col = 'genres', ci = False, kind = 'line',
#                hue = 'genres', height = 3)
#ax = sns.relplot(data = df_genres_top5, x = 'year', y = 'speechiness', col = 'genres', ci = False, kind = 'line',
#                hue = 'genres', height = 3)
#ax = sns.relplot(data = df_genres_top5, x = 'year', y = 'acousticness', col = 'genres', ci = False, kind = 'line',
#                hue = 'genres', height = 3)
#ax = sns.relplot(data = df_genres_top5, x = 'year', y = 'tempo', col = 'genres', ci = False, kind = 'line',
#                hue = 'genres', height = 3)
plt.show()

# ## Is genre a good predictor for energy level of songs?

# + endofcell="--"
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

target = df_energy['energy'].values
categorical = OneHotEncoder().fit_transform(df_energy[["genres"]].values).toarray()
numerical = df_energy[["energy"]].values
data = np.append(categorical, numerical, axis=1)

linear_model = LinearRegression()
linear_model.fit(X=data, y=target)
predicted = linear_model.predict(data)

q2_mse = mean_squared_error(target, predicted)
q2_r2 = r2_score(target, predicted)

# Baseline 
average = np.mean(df_energy["energy"])
baseline = np.full(predicted.shape, average)
mse_baseline = mean_squared_error(target, baseline)
r2_baseline = r2_score(target, baseline)

print("MSE:", q2_mse, "r^2:", q2_r2)
print('Model MSE Baseline:', mse_baseline)
print('Model r^2 Baseline:', r2_baseline)
# -

# 
# --

# Here we are predicting energy of songs (target column) based on the categorical variable genre. We used OneHotEncoder because genres are nomial and not an ordinal variable. The model's MSE is extremely small and r^2 is 1, which means the model is able to use genre to predict energy of a song 100% of the time. This is a sign, the model may be overfitting the data, meaning it is fitting the noise or random fluctuations in the data instead of the underlying pattern. The model has a smaller MSE than the baseline model, indicating the model has better performance and better fit to the data. The r^2 of the baseline is 0, which is reasonable since it's predicting the mean energy of a song (a constant).

# ## Model with training and testing sets


# +
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.dummy import DummyRegressor

#df_model = df_energy[(df_energy['energy'].notna()) & (df_energy['genres'].notna())]
#target = df_model['energy'].values
#data = df_model['genres'].values

#df_model = df_energy[(df_energy['danceability'].notna()) & (df_energy['genres'].notna())]
#target = df_model['danceability'].values
#data = df_model['genres'].values

#df_model = df_energy[(df_energy['speechiness'].notna()) & (df_energy['genres'].notna())]
#target = df_model['speechiness'].values
#data = df_model['genres'].values

#df_model = df_energy[(df_energy['acousticness'].notna()) & (df_energy['genres'].notna())]
#target = df_model['acousticness'].values
#data = df_model['genres'].values

#df_model = df_energy[(df_energy['tempo'].notna()) & (df_energy['genres'].notna())]
#target = df_model['tempo'].values
#data = df_model['genres'].values

df_model = df_model[(df_model['genres'] == 'album rock') |
                    (df_model['genres'] == 'dance pop') |
                    (df_model['genres'] == 'contemporary r&b') |
                    (df_model['genres'] == 'adult standards') |
                    (df_model['genres'] == 'classic soul')]

train_data, test_data, train_target, test_target = train_test_split(
    data, target, test_size=0.25, random_state=370)

encoder = OneHotEncoder(handle_unknown='ignore')
cat_train = encoder.fit_transform(train_data.reshape(-1, 1))
cat_test = encoder.transform(test_data.reshape(-1, 1))

linear_model = LinearRegression()
linear_model.fit(X=cat_train, y=train_target)
predicted = linear_model.predict(cat_test)

mse = mean_squared_error(test_target, predicted)
r2 = r2_score(test_target, predicted)

df_plot = pd.DataFrame({'Actual': test_target, 'Predicted': predicted, 'Genre': test_data})
sns.relplot(x='Actual', y='Predicted', hue='Genre', data=df_plot, alpha=0.5)

plt.xlabel("Actual values")
plt.ylabel("Predicted values")
plt.title("Predicted versus actual values by genre")
plt.show

print("MSE:", mse, "r^2:", r2)

dummy_model = DummyRegressor(strategy='mean')
dummy_model.fit(X=cat_train, y=train_target)
baseline_predicted = dummy_model.predict(cat_test)

baseline_mse = mean_squared_error(test_target, baseline_predicted)
baseline_r2 = r2_score(test_target, baseline_predicted)

plt.scatter(test_target, baseline_predicted, color = 'orange')

print("Baseline MSE:", baseline_mse, "Baseline r^2:", baseline_r2)
