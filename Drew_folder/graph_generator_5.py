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

# # Merge datasets
merged_df = pd.merge(df_2[['State', 'Violent_Crimes']], unempl_agg, on='State', how='inner')
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
# plt.savefig('Obesity_vs_Unemployment_Heatmap.png')
plt.show()


# Plot scatter plot
sample_df = final_df.sample(frac=0.10, random_state=42)
sample_df.plot.scatter(
    x='Unemployment_percentage_per_state', 
    y='Violent_Crimes', 
    color='blue'
)
sns.regplot(
    x='Unemployment_percentage_per_state',
    y='Violent_Crimes',
    data=final_df,
    scatter_kws={"color": "blue"},
    line_kws={"color": "red"}
)
plt.title('Relationship between Unemployment Rate and Crimes Committed per US State')
plt.xlabel('Unemployment Rate(%)')
plt.ylabel('# Of Crimes Commited')
plt.savefig('Crime_vs_Unemployment_Scatterplot.png')
plt.show()


