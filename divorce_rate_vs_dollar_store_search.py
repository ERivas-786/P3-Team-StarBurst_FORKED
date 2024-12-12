import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
path = './Datasets/dollar_store_google_searches.csv'
path2 = './Datasets/divorce_rates.csv'

df = pd.read_csv(path).rename(columns={'Month':'YEAR', 'Dollar store near me: (United States)' : 'Dollar_store_search_interest_over_time'})
df['YEAR'] = pd.to_datetime(df['YEAR'], format='%Y-%m').dt.year
df_2 = pd.read_csv(path2)

# # Aggregate unemployment data by State/Area
# unemployment_agg = df.groupby('State/Area')['Unemployment_percentage_per_state'].mean().reset_index()
# Replace "<1" with a numeric value (e.g., 0.5 or 0)
df['Dollar_store_search_interest_over_time'] = df['Dollar_store_search_interest_over_time'].replace('<1', '0.5')

# Ensure the column is numeric
df['Dollar_store_search_interest_over_time'] = pd.to_numeric(df['Dollar_store_search_interest_over_time'], errors='coerce')

# # Merge datasets
merged_df = pd.merge(df[['YEAR','Dollar_store_search_interest_over_time']], df_2[['YEAR', 'RATE']], on='YEAR', how='inner')

# # Handle missing values (if any)
final_df = merged_df.dropna().reset_index(drop=True)

# # Print the final DataFrame
# print(final_df)

# # Compute correlation matrix
correlation_matrix = final_df[['YEAR', 'Dollar_store_search_interest_over_time', 'RATE']].corr()
print(correlation_matrix)

# # Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Google Search for Dollar Stores and Divorce Rates")
filePath = './Analysis_results/'
plt.savefig(filePath + 'Google_Search_Dollar_Store_vs_Divorce_Rate_Heatmap.png')
plt.show()

aggregated_df = merged_df.groupby('YEAR', as_index=False).mean()

# Create a dual-axis line graph
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the first line (primary y-axis)
ax1.plot(aggregated_df['YEAR'], aggregated_df['Dollar_store_search_interest_over_time'], 'o--', color='blue', label='Dollar Store Search Interest')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Dollar Store Search Interest', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add secondary y-axis for the second line
ax2 = ax1.twinx()
ax2.plot(aggregated_df['YEAR'], aggregated_df['RATE'], 'o--', color='red', label='Divorce Rate')
ax2.set_ylabel('Divorce Rate (Per 100,000)', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add a title and grid
plt.title('Dollar Store Search Interest and Divorce Rate Over Time (r=-0.01)', fontsize=14)
ax1.grid(True, linestyle=':')

# Show the plot
plt.tight_layout()
filePath = './Analysis_results/'
plt.savefig(filePath + 'Google_Search_Dollar_Store_vs_Divorce_Rate_LineGraph.png')
plt.show()
