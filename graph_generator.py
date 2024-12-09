import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
path = './Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States(1).csv'
df = pd.read_csv(path)

path2 = './annual_gold_rate.csv'
df_2 = pd.read_csv(path2)
df_2 = df_2.rename(columns={'Date': 'YEAR_NUM'})

# Select relevant columns
df_selected = df[['ESTIMATE', 'YEAR_NUM']]
df_selected_2 = df_2[['YEAR_NUM', 'USD']]

merged_df = pd.merge(df, df_2, on='YEAR_NUM')
final_df = merged_df[['ESTIMATE', 'YEAR_NUM', 'USD']]

# final_df.dropna()
# final_df.reindex(axis = 0)

# Compute the correlation matrix
correlation_matrix = final_df.corr()
print(correlation_matrix)


# Plot the heatmap
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title("Correlation Heatmap")
# plt.show()
