import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
socialmediadata = pd.read_csv("./datasets/socialmedia.csv",usecols = ["User Follower Count","DateTime"])  
airqualitydata = pd.read_csv("./datasets/airquality.csv", usecols = ["Date", "CO"], nrows=24)  

#convert date and time to datetime
socialmediadata['Month'] = pd.to_datetime(socialmediadata['DateTime']).dt.month
socialmediadata.drop(columns=['DateTime'], inplace=True)
airqualitydata['Month'] = pd.to_datetime(airqualitydata['Date']).dt.month
airqualitydata.drop(columns=['Date'], inplace=True)


# Merge datasets on 'Year'
merged_data = pd.merge(socialmediadata, airqualitydata, on="Month")

# Calculate correlation matrix
correlation_matrix = merged_data.corr()

print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot MaxT on the left y-axis
ax1.plot(merged_data["Month"], merged_data["User Follower Count"], label="User Follower Count", color='blue', marker='o')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('User Follower Count', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add a secondary y-axis for Visitors
ax2 = ax1.twinx()
ax2.plot(merged_data["Month"], merged_data["CO"], label="air quality CO", color='green', marker='s')
ax2.set_ylabel('CO', fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Title and grid
plt.title('follower count vs CO air quality', fontsize=14)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legends for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()

