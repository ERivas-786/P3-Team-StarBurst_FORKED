import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
path = './Unemployment_in_America_Per_US_State.csv'
path2 = './US_Obesity_Rates.csv'

df = pd.read_csv(path).rename(columns={'Percent (%) of Labor Force Unemployed in State/Area': 'Unemployment_percentage_per_state'})
df_2 = pd.read_csv(path2).rename(columns={'NAME': 'State/Area'})

# Aggregate unemployment data by State/Area
unemployment_agg = df.groupby('State/Area')['Unemployment_percentage_per_state'].mean().reset_index()

# Merge datasets
merged_df = pd.merge(unemployment_agg, df_2[['State/Area', 'Obesity']], on='State/Area', how='inner')

# Handle missing values (if any)
final_df = merged_df.dropna().reset_index(drop=True)

# Print the final DataFrame
print(final_df)

# Compute correlation matrix
correlation_matrix = final_df[['Obesity', 'Unemployment_percentage_per_state']].corr()
print(correlation_matrix)

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Plot scatter plot
final_df.plot.scatter(
    x='Obesity', 
    y='Unemployment_percentage_per_state', 
    color='blue'
)
plt.xlabel('Obesity')
plt.ylabel('Unemployment Percentage Per State')
plt.show()
