import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
layoffsdata = pd.read_csv("./datasets/layoffs.csv",usecols = ["Date","total_laid_off"])  
moviedata = pd.read_csv("./datasets/movie.csv", usecols = ["Year", "Worldwide"]) 

#convert datetime to year
layoffsdata['Year'] = pd.to_datetime(layoffsdata['Date'], format='%Y-%m-%d').dt.year
layoffsdata.drop(columns=['Date'], inplace=True)
moviedata["Worldwide"] = moviedata["Worldwide"].str.replace(',','').astype(int)

# Merge datasets on 'Year'
merged_data = pd.merge(layoffsdata, moviedata, on="Year")


# Calculate correlation matrix
correlation_matrix = merged_data.corr()

print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot MaxT on the left y-axis
ax1.plot(merged_data["Year"], merged_data["total_laid_off"], label="Total layoffs", color='blue', marker='o')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Total laid off', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add a secondary y-axis for Visitors
ax2 = ax1.twinx()
ax2.plot(merged_data["Year"], merged_data["Worldwide"], label="World wide amount", color='green', marker='s')
ax2.set_ylabel('World wide amount', fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Title and grid
plt.title('Layoffs vs Worldwide amount', fontsize=14)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legends for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()