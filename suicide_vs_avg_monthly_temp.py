import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

##TEMP VS SUICIDE YEARLY

# Load datasets
path = './Datasets/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States(1).csv'
path2 = './Datasets/average_monthly_temperature_by_state_1950-2022.csv'

df = pd.read_csv(path).rename(columns={'YEAR': 'Year', 'ESTIMATE': 'Suicide_Rate'})

df_2 = pd.read_csv(path2).rename(columns={'year': 'Year'})




# # Aggregate unemployment data by State/Area
suicide_agg = df.groupby('Year')['Suicide_Rate'].mean().reset_index()
temp_agg = df_2.groupby('Year')['average_temp'].mean().reset_index()


# # Merge datasets
merged_df = pd.merge(suicide_agg, temp_agg, on='Year', how='inner')
final_df = merged_df.dropna().reset_index(drop=True)

print(final_df)

# # Print the final DataFrame

# # Compute correlation matrix
correlation_matrix = final_df[['Year', 'average_temp', 'Suicide_Rate']].corr()
print(correlation_matrix)

# # Plot heatmap
# plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Suicide vs Temperature")
filePath = './Analysis_results/'
plt.savefig(filePath + 'Suicide_vs_Monthly_Temp_Heatmap.png')
plt.show()


fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the first line (primary y-axis)
ax1.plot(merged_df['Year'], merged_df['average_temp'], 'o--', color='blue', label='Dollar Store Search Interest')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Temp Across the US (F)', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add secondary y-axis for the second line
ax2 = ax1.twinx()
ax2.plot(merged_df['Year'], merged_df['Suicide_Rate'], 'o--', color='red', label='Divorce Rate')
ax2.set_ylabel('Suicide Rate (Per 100,000)', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add a title and grid
plt.title('Correlation Between Suicide Rates and Average Yearly Temperature', fontsize=14)
ax1.grid(True, linestyle=':')

# Show the plot
plt.tight_layout()
filePath = './Analysis_results/'
plt.savefig(filePath + 'Suicide_Rate_vs_Temperature.png')
plt.show()
