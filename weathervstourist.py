import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
weatherdata = pd.read_excel("./datasets/weather.xlsx",usecols = ["Date","MaxT"])  
tourismdata = pd.read_csv("./datasets/tourist.csv", usecols = ["Year", "Visitors"])  

#convert datetime to year
weatherdata['Year'] = pd.to_datetime(weatherdata['Date'], format='%m/%d/%Y').dt.year
weatherdata.drop(columns=['Date'], inplace=True)

# Merge datasets on 'Year'
merged_data = pd.merge(weatherdata, tourismdata, on="Year")


# Calculate correlation matrix
correlation_matrix = merged_data.corr()

print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot MaxT on the left y-axis
ax1.plot(merged_data["Year"], merged_data["MaxT"], label="MaxT", color='blue', marker='o')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('MaxT', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add a secondary y-axis for Visitors
ax2 = ax1.twinx()
ax2.plot(merged_data["Year"], merged_data["Visitors"], label="Tourism Visitors", color='green', marker='s')
ax2.set_ylabel('Visitors', fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Title and grid
plt.title('MaxT vs Visitors', fontsize=14)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legends for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()
