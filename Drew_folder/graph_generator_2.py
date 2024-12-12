import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
path = './Datasets/average_monthly_temperature_by_state_1950-2022.csv'
path2 = './Datasets/avocado.csv'

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
sample_df = final_df.sample(frac=0.10, random_state=42)


fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(final_df['Year'], final_df['average_temp'], color='red', label='Average Temperature')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Temperature (°C)', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Create the second Y-axis for avocado prices
ax2 = ax1.twinx()
ax2.plot(final_df['Year'], final_df['AveragePrice'], color='blue', label='Average Avocado Price')
ax2.set_ylabel('Average Avocado Price (USD)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Title and legend
plt.title('Yearly Trends: Average Temperature vs. Avocado Prices')
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Save and show the plot
filePath = './Analysis_results/'
plt.savefig(filePath + 'Temperature_vs_Avocado_Prices_LineGraph.png')
plt.show()
