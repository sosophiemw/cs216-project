import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast
import datetime
from sklearn.preprocessing import OneHotEncoder

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
df_grouped = df_grouped.groupby(['year']).mean()
# print(df_grouped)

# +
target = df_energy['energy'].values
# categorical = OneHotEncoder().fit_transform(merged_df[["genre"]].values).toarray()
# numerical = penguins[["bill_length_mm", "bill_depth_mm"]].values
# data = np.append(categorical, numerical, axis=1)

# linear_model = LinearRegression()
# linear_model.fit(X=data, y=target)
# predicted = linear_model.predict(data)

# q2_mse = mean_squared_error(target, predicted)
# q2_r2 = r2_score(target, predicted)

# Baseline 
# average = np.mean(df_energy["energy"])
# baseline = np.full(predicted.shape, average)
# mse_baseline = mean_squared_error(target, baseline)
# r2_baseline = r2_score(target, baseline)

# print("MSE:", q2_mse, "r^2:", q2_r2)
# print('Model MSE Baseline:', mse_baseline)
# print('Model r^2 Baseline:', r2_baseline)
# -

# Here we are predicting energy of songs (target column) based on the categorical variable genre. The model's MSE is ... and r^2 is.., This indicates...


