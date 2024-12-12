import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#AVOCADO PRICE VS SUICIDE RATES

# Load datasets
path = './Datasets/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States(1).csv'
path2 = './Datasets/avocado.csv'

df = pd.read_csv(path).rename(columns={'YEAR': 'Year'})
df_2 = pd.read_csv(path2)
df_2['Date'] = pd.to_datetime(df_2['Date'])
df_2['Year'] = df_2['Date'].dt.year



# # Aggregate unemployment data by State/Area
# avocado_agg = df.groupby('Year')['AveragePrice'].mean().reset_index()

# # Merge datasets
merged_df = pd.merge(df[['Year', 'ESTIMATE']], df_2[['Year', 'AveragePrice']], on='Year', how='inner')
final_df = merged_df.dropna().reset_index(drop=True)

print(final_df)

# # Print the final DataFrame

# # Compute correlation matrix
correlation_matrix = final_df[['Year', 'AveragePrice', 'ESTIMATE']].corr()
print(correlation_matrix)

# # Plot heatmap
# plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Suicide vs Avocado")
# plt.savefig('Obesity_vs_Unemployment_Heatmap.png')
plt.show()

# # Plot scatter plot
# final_df.plot.scatter(
#     x='Obesity', 
#     y='Unemployment_percentage_per_state', 
#     color='blue'
# )
# plt.title('Relationship between Unemployment Rate and Obesity per US State')
# plt.xlabel('Obesity')
# plt.ylabel('Unemployment Percentage Per State')
# plt.savefig('Obesity_vs_Unemployment_Scatterplot.png')
# plt.show()
