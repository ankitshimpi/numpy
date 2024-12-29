import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def calculate_overweight(df):
  df['height_m'] = df['height'] / 100 
  df['bmi'] = df['weight'] / (df['height_m'] ** 2)
  df['overweight'] = (df['bmi'] > 25).astype(int)
  df.drop('height_m', axis=1, inplace=True)  
  return df
def normalize_data(df):
  df['cholesterol'] = df['cholesterol'].replace(1, 0)
  df['cholesterol'] = df['cholesterol'].replace(2, 1)
  df['gluc'] = df['gluc'].replace(1, 0)
  df['gluc'] = df['gluc'].replace(2, 1)
  return df
def draw_cat_plot(df):
  df_cat = pd.melt(df,
                   id_vars=['cardio'],
                   var_name='feature',
                   value_name='count')
  df_cat_grouped = df_cat.groupby(['cardio', 'feature']).agg(count=('count', 'sum')).unstack().reset_index()
  df_cat_grouped.rename(columns={'cardio': 'has_cardio'}, inplace=True)
  fig = sns.catplot(x='feature', y='count', hue='has_cardio', data=df_cat_grouped, kind='bar')
  plt.show()
  return fig
def draw_heat_map(df):
  df_filtered = df[df['ap_lo'] <= df['ap_hi']]  
  df_filtered = df_filtered[(df_filtered['height'] >= df_filtered['height'].quantile(0.025))]  
  df_filtered = df_filtered[df_filtered['height'] <= df_filtered['height'].quantile(0.975)]
  df_filtered = df_filtered[(df_filtered['weight'] >= df_filtered['weight'].quantile(0.025))]  
  df_filtered = df_filtered[df_filtered['weight'] <= df_filtered['weight'].quantile(0.975)]
  corr = df_filtered.corr()
  mask = np.triu(np.ones(corr.shape)) 
  fig, ax = plt.subplots(figsize=(10, 10))
  sns.heatmap(corr, mask=mask, vmax=1, vmin=-1, annot=True, ax=ax)
  plt.show()
  return fig
df = pd.read_csv('medical_examination.csv')
df = calculate_overweight(df.copy())  
df = normalize_data(df.copy())

draw_cat_plot(df.copy())
draw_heat_map(df.copy())
