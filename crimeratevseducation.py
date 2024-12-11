import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
crimedata = pd.read_csv("./datasets/UScrimerates.csv",usecols = ["Year","Total"])  
educationwagedata = pd.read_csv("./datasets/educationwages.csv", usecols = ["Year", "lesshs"])  


# Merge datasets on 'Year'
merged_data = pd.merge(crimedata, educationwagedata, on="Year")


# Calculate correlation matrix
correlation_matrix = merged_data.corr()

print(correlation_matrix)

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot MaxT on the left y-axis
ax1.plot(merged_data["Year"], merged_data["Total"], label="Total crimes", color='blue', marker='o')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Total crimes', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add a secondary y-axis for Visitors
ax2 = ax1.twinx()
ax2.plot(merged_data["Year"], merged_data["lesshs"], label="wages for highschool dropouts", color='green', marker='s')
ax2.set_ylabel('wages', fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Title and grid
plt.title('Crimerates vs wages of highschool dropouts', fontsize=14)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legends for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()