import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def clean_data(df):
  q1 = df['page_views'].quantile(0.025)
  q3 = df['page_views'].quantile(0.975)
  return df.query('page_views >= @q1 and page_views <= @q3')
def draw_line_plot(df):
  fig, ax = plt.subplots(figsize=(12, 6))
  ax.plot(df.index, df['page_views'])
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

def draw_bar_plot(df):
  df_avg_monthly = df.resample('M')['page_views'].mean().unstack()
  fig, ax = plt.subplots(figsize=(10, 6))
  df_avg_monthly.plot(kind='bar', ax=ax)
  plt.title('Months')
  plt.xlabel('Years')
  plt.ylabel('Average Page Views')
  plt.xticks(rotation=0)
  plt.legend(title='Month')
  plt.tight_layout()
  plt.show()

def draw_box_plot(df):
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
  sns.boxplot(
      x = "year",
      y = "page_views",
      showmeans=True,
      data=df
  )
  ax1.set_title('Year-wise Box Plot (Trend)')
  ax1.set_xlabel('Year')
  ax1.set_ylabel('Page Views')

  sns.boxplot(
      x = "month",
      y = "page_views",
      showmeans=True,
      data=df.sort_values(by=['year', 'month'])
  )
  ax2.set_title('Month-wise Box Plot (Seasonality)')
  ax2.set_xlabel('Month')
  ax2.set_ylabel('Page Views')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()
df = pd.read_csv("fcc-forum-pageviews.csv")
df.set_index('date', inplace=True)
df_clean = clean_data(df.copy())
draw_line_plot(df_clean.copy())
draw_bar_plot(df_clean.copy())
draw_box_plot(df_clean.copy())
