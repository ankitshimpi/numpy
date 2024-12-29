import pandas as pd
def analyze_demographic_data(data_path):
  df = pd.read_csv(data_path)
  race_counts = df['race'].value_counts()
  average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)
  percent_bachelors = (df['education'] == 'Bachelors').mean() * 100
  df_advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  df_advanced_education_gt_50k = df_advanced_education[df_advanced_education['salary'] == '>50K']
  percent_advanced_education_gt_50k = (len(df_advanced_education_gt_50k) / len(df_advanced_education)) * 100
  df_no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  df_no_advanced_education_gt_50k = df_no_advanced_education[df_no_advanced_education['salary'] == '>50K']
  percent_no_advanced_education_gt_50k = (len(df_no_advanced_education_gt_50k) / len(df_no_advanced_education)) * 100
  min_hours_worked = df['hours-per-week'].min()
  df_min_hours = df[df['hours-per-week'] == min_hours_worked]
  df_min_hours_gt_50k = df_min_hours[df_min_hours['salary'] == '>50K']
  percent_min_hours_gt_50k = (len(df_min_hours_gt_50k) / len(df_min_hours)) * 100
  df_gt_50k_by_country = (df[df['salary'] == '>50K']
                          .groupby('native-country')
                          .size()
                          .to_frame(name='count')
                          .reset_index()
                          .merge(df.groupby('native-country').size().to_frame(name='total'), on='native-country')
                          .assign(percent=lambda x: (x['count'] / x['total']) * 100)
                          .sort_values(by='percent', ascending=False)
                          .head(1))
  highest_earning_country = df_gt_50k_by_country['native-country'].tolist()[0]
  highest_earning_country_percent = df_gt_50k_by_country['percent'].tolist()[0].round(1)
  df_india_gt_50k = df[(df['native-country'] == 'India') & (df['
