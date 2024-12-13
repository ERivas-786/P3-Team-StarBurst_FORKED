import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

##Crime VS Unemployment

# Load datasets
path = './Datasets/Unemployment_in_America_Per_US_State.csv'
path2 = './Datasets/state_crime.csv'

df = pd.read_csv(path).rename(columns={'State/Area': 'State', 'Percent (%) of Labor Force Unemployed in State/Area': 'Unemployment_percentage_per_state'})

df_2 = pd.read_csv(path2).rename(columns={'Data.Rates.Violent.All': 'Violent_Crimes'})

# # Aggregate unemployment data by State/Area

unempl_agg = df.groupby('State')['Unemployment_percentage_per_state'].mean().reset_index()
crime_agg = df_2.groupby('State')['Violent_Crimes'].mean().reset_index()

# # Merge datasets
merged_df = pd.merge(crime_agg, unempl_agg, on='State', how='inner')
final_df = merged_df.dropna().reset_index(drop=True)

print(final_df)

# # Print the final DataFrame

# # Compute correlation matrix
correlation_matrix = final_df[['Violent_Crimes', 'Unemployment_percentage_per_state']].corr()
print(correlation_matrix)

# # Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Unemployment Rate vs Violent Crime Rate")
filePath = './Analysis_results/'
plt.savefig(filePath + 'Crime_vs_Unemployment_Heatmap.png')
plt.show()


# Plot scatter plot
plt.figure(figsize=(12, 8))  # Set the width to 12 inches and height to 8 inches

# Scatterplot
sns.scatterplot(
    x='Unemployment_percentage_per_state',
    y='Violent_Crimes',
    data=final_df,
    color='blue',
    s=60,  # Adjusted marker size for better visibility on larger plot
    edgecolor='black',  # Add edge color to markers for better definition
    alpha=0.7  # Transparency for markers
)

# Regression line
sns.regplot(
    x='Unemployment_percentage_per_state',
    y='Violent_Crimes',
    data=final_df,
    scatter=False,  # Hide default scatter to avoid overlap
    line_kws={"color": "red", "linewidth": 2},  # Adjusted line width
)

# Add title and labels
plt.title('Relationship Between Unemployment Rate and Violent Crimes', fontsize=16, fontweight='bold')
plt.xlabel('Unemployment Rate (%)', fontsize=14)
plt.ylabel('No. of Violent Crimes (Per 100,000 individuals)', fontsize=14)

# Save and display the plot
filePath = './Analysis_results/'
plt.savefig(filePath + 'Crime_vs_Unemployment_Scatterplot.png')
plt.show()
