import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#AVOCADO PRICE VS SUICIDE RATES

# Load datasets
path = './Datasets/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States(1).csv'
path2 = './Datasets/avocado.csv'

df = pd.read_csv(path).rename(columns={'YEAR': 'Year', 'ESTIMATE': 'SR_Percentage'})
df_2 = pd.read_csv(path2)
df_2['Date'] = pd.to_datetime(df_2['Date'])
df_2['Year'] = df_2['Date'].dt.year



# Aggregate suicide rate data by year
suicide_agg = df.groupby('Year', as_index=False)['SR_Percentage'].mean()

# Aggregate avocado price data by year
avocado_agg = df_2.groupby('Year', as_index=False)['AveragePrice'].mean()

# Merge the aggregated datasets
merged_df = pd.merge(suicide_agg, avocado_agg, on='Year', how='inner')

# Drop NaN values (if any)
final_df = merged_df.dropna().reset_index(drop=True)

# Print the final DataFrame
print(final_df)



print(final_df)

# # Print the final DataFrame

# # Compute correlation matrix
correlation_matrix = final_df[['Year', 'AveragePrice', 'SR_Percentage']].corr()
print(correlation_matrix)

# # Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Suicide Rate vs Avocado Price")
filePath = './Analysis_results/'
plt.savefig(filePath + 'Suicide_Rates_vs_Avocado_Prices_Heatmap.png')
plt.show()

# Plotting Line Graph
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot suicide rates on the primary y-axis
ax1.plot(final_df['Year'], final_df['SR_Percentage'], color='red', label='Suicide Rate')
ax1.set_xlabel('Year')
ax1.set_ylabel('Suicide Rate (Per 100,000)', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Create the second Y-axis for avocado prices
ax2 = ax1.twinx()
ax2.plot(final_df['Year'], final_df['AveragePrice'], color='blue', label='Average Avocado Price')
ax2.set_ylabel('Average Avocado Price (USD)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Title and legend
plt.title('Yearly Trends: Suicide Rates (US) vs. Avocado Prices')
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Save and show the plot
filePath = './Analysis_results/'
plt.savefig(filePath + 'Suicide_Rates_vs_Avocado_Prices_LineGraph.png')
plt.show()

