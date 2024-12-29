import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
def predict_sea_level(data_path):
  df = pd.read_csv(data_path)
  plt.figure(figsize=(10, 6))
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  slope, intercept, r_value, p_value, std_err = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  line_all_data = slope * df['Year'] + intercept
  predicted_level_all_data = slope * 2050 + intercept
  plt.plot(df['Year'], line_all_data, color='red')
  df_2000_onwards = df[df['Year'] >= 2000]
  slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = stats.linregress(df_2000_onwards['Year'], df_2000_onwards['CSIRO Adjusted Sea Level'])
  line_2000_onwards = slope_2000 * df['Year'] + intercept_2000
  predicted_level_2000_onwards = slope_2000 * 2050 + intercept_2000
  plt.plot(df['Year'], line_2000_onwards, color='green')
  plt.text(2050, predicted_level_all_data + 0.05, f'Predicted 2050 Level (All Data): {predicted_level_all_data:.2f} inches', ha='center', color='red')
  plt.text(2050, predicted_level_2000_onwards + 0.05, f'Predicted 2050 Level (Since 2000): {predicted_level_2000_onwards:.2f} inches', ha='center', color='green')
  plt.tight_layout()
  plt.show()
  return {
      'predicted_level_all_data': predicted_level_all_data,
      'predicted_level_2000_onwards': predicted_level_2000_onwards
  }
results = predict_sea_level('epa-sea-level.csv')
print(results)
