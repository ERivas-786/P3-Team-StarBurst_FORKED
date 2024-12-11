import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
path = './average_monthly_temperature_by_state_1950-2022.csv'
path2 = './avocado.csv'

df = pd.read_csv(path).rename(columns={'year': 'Year'})
df_2 = pd.read_csv(path2)
df_2['Date'] = pd.to_datetime(df_2['Date'])
df_2['Year'] = df_2['Date'].dt.year



# # Aggregate unemployment data by State/Area
# unemployment_agg = df.groupby('State/Area')['Unemployment_percentage_per_state'].mean().reset_index()

# # Merge datasets
df_agg = df.groupby('Year')['average_temp'].mean().reset_index()
df_2_agg = df_2.groupby('Year')['AveragePrice'].mean().reset_index()

# Merge the aggregated data
merged_df = pd.merge(df_agg, df_2_agg, on='Year', how='inner')

# Remove rows with NaN values
final_df = merged_df.dropna().reset_index(drop=True)

# Print the aggregated DataFrame
print(final_df)

# # Print the final DataFrame

# # Compute correlation matrix
correlation_matrix = final_df[['Year', 'AveragePrice', 'average_temp']].corr()
print(correlation_matrix)

# # Plot heatmap
# plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Temp vs Avocado")
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
