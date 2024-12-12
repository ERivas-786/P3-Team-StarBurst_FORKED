import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
weatherdata = pd.read_excel("./datasets/weather.xlsx", usecols=["Date", "Cum_Rain"])  
tourismdata = pd.read_csv("./datasets/tourist.csv", usecols=["Year", "Visitors"])  

# Convert datetime to year (let pandas infer the format)
weatherdata['Year'] = pd.to_datetime(weatherdata['Date']).dt.year
weatherdata.drop(columns=['Date'], inplace=True)

# Group by Year and get the max value of 'Cum_Rain' and 'Visitors'
groupedweatherdata = weatherdata.groupby('Year')['Cum_Rain'].max()
groupedtouristdata = tourismdata.groupby('Year')['Visitors'].max()

# Merge datasets on 'Year'
merged_data = pd.merge(groupedweatherdata, groupedtouristdata, on="Year")

# Reset index to convert 'Year' from index to column
merged_data.reset_index(inplace=True)


# Calculate correlation matrix
correlation_matrix = merged_data.corr()
print(correlation_matrix)

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("Weather vs Tourist correlation_heatmap.png") 
plt.show()

# Plotting the data
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Cum_Rain on the left y-axis
ax1.plot(merged_data["Year"], merged_data["Cum_Rain"], label="Cumulative Rainfall", color='blue', marker='o')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Cummulative Rainfall', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add a secondary y-axis for Visitors
ax2 = ax1.twinx()
ax2.plot(merged_data["Year"], merged_data["Visitors"], label="Visitors", color='green', marker='s')
ax2.set_ylabel('Visitors', fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Title and grid
plt.title('Rainfall vs Visitors', fontsize=14)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legends for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.savefig("Weathervstourist.png") 
plt.show()