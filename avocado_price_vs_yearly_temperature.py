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

# Check the columns of the temperature data to see if it includes a 'State' or equivalent column
print(df.columns)

# Filter the temperature data to only include Florida (assuming the column name is 'State')
df_florida = df[df['State'] == 'Florida']  # Replace 'State' with the actual column name

# Aggregate temperature data for Florida
df_florida_agg = df_florida.groupby('Year')['average_temp'].mean().reset_index()

# Aggregate avocado price data by year
df_2_agg = df_2.groupby('Year')['AveragePrice'].mean().reset_index()

# Merge the aggregated data
merged_df = pd.merge(df_florida_agg, df_2_agg, on='Year', how='inner')

# Remove rows with NaN values
final_df = merged_df.dropna().reset_index(drop=True)

# Print the final DataFrame
print(final_df)

# Compute the correlation matrix
correlation_matrix = final_df[['Year', 'AveragePrice', 'average_temp']].corr()
print(correlation_matrix)

# Plot heatmap of the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Florida Temperature vs Avocado Prices")
filePath = './Analysis_results/'
plt.savefig(filePath + 'Avocado_Prices_vs_Florida_Temperature_Heatmap.png')
plt.show()

# Plotting the Line Graph for Florida Temperature vs Avocado Prices
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(final_df['Year'], final_df['average_temp'], color='red', label='Average Temperature')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Temperature (°F)', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Create the second Y-axis for avocado prices
ax2 = ax1.twinx()
ax2.plot(final_df['Year'], final_df['AveragePrice'], color='blue', label='Average Avocado Price')
ax2.set_ylabel('Average Avocado Price (USD)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Title and legend
plt.title('Yearly Trends: Average Florida Temperature(F) vs Avocado Prices(USD)')
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Save and show the plot
filePath = './Analysis_results/'
plt.savefig(filePath + 'Avocado_Prices_vs_Florida_Temp_LineGraph.png')
plt.show()
