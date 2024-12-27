import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
socialmediadata = pd.read_csv("./datasets/socialmedia.csv",usecols = ["User Follower Count","DateTime"])  
airqualitydata = pd.read_csv("./datasets/airquality.csv", usecols = ["Date", "CO"], nrows=24)  

#convert date and time to datetime
socialmediadata['Month'] = pd.to_datetime(socialmediadata['DateTime']).dt.month
socialmediadata.drop('DateTime', axis=1, inplace=True)
airqualitydata['Month'] = pd.to_datetime(airqualitydata['Date']).dt.month
airqualitydata.drop(columns=['Date'], inplace=True)

# Group by Year and get the max value of 'Cum_Rain' and 'Visitors'
groupedsocialmediadata = socialmediadata.groupby('Month')['User Follower Count'].mean()
groupedairqualitydata = airqualitydata.groupby('Month')['CO'].mean()
'''
some here'''

# Merge datasets on 'Year'
merged_data = pd.merge(groupedsocialmediadata, groupedairqualitydata, on="Month")
'''more merge conflicts
dfsopiodiospjfplksdf'''
#re for find pattern
date_patterns = re.compile(r'(date|year)', re.IGNORECASE)
#dftgdfsdfgssdfghsdfghsdfdf
print("fffkjfkfkfkfk")
# rename date|year columns to 'Year/Date'
def change_column_header(cols):
    changed = []
    for item in cols:
        if date_patterns.search(item):
            changed.append('Year/Date') 
        # else:
            changed.append(item)
    return changed
# Reset index to convert 'Year' from indgit ex to column
merged_data.reset_index(inplace=True)
#something 
#John's comment
# 2

'''
MERGE CONFLICT HERE?????
?????????????????
???????????????????
????????????????????????????????????????????????????????
'''

# Calculate correlation matrix
correlation_matrix = merged_data.corr()

print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("Socialmedia vs Airquality(CO) correlation_heatmap.png") 
plt.show()

#ROMEO WAS HERE!!!!!!!!!!!!!!

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


# Sneak a little merge conflict here >:) - Alexi

def merge_that_conflict():
    print("Uh oh!")

# boop

# Title and grid
plt.title('follower count vs CO air quality 2024', fontsize=14)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add legends for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.savefig("Socialmediavsairqualityplot.png") 
plt.show()

