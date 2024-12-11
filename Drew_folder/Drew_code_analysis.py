import sys
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


run = True

while(run) :

    selection = input("Enter selection: ")

    if selection.lower() == 'o' : 
        print(''' list of options: 
                1 - Choose datasets to compare
                2 - 
                3 - 
                4 - 
                5 -  
                6 - 
                7 - 
                8 - 
                9 - 
                10 - 
                11 - Or q to quit. ''')

    elif selection == "1" : 

        # Load the first dataset
        path = 'Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States(1).csv'
        df = pd.read_csv(path)

        # Load the second dataset
        path2 = 'annual_gold_rate.csv'
        df_2 = pd.read_csv(path2)
        df_2 = df_2.rename(columns={'Date': 'YEAR'})

        # Select relevant columns
        df_selected = df[['ESTIMATE', 'YEAR']]
        df_selected_2 = df_2[['YEAR', 'USD']]


        # Merge Dataframes on common columns for analysis
        merged_df = pd.merge(df, df_2, on='YEAR')
        final_df = merged_df[['ESTIMATE', 'YEAR', 'USD']]


        # Filling blank entries for continuity
        final_df.dropna()
        final_df.reindex(axis = 0)

        # print(final_df.head())  # View the first few rows
        # print(merged_df.info())  # Inspect data types and non-null counts
        # print(merged_df.describe())  # View summary statistics


        # Compute the correlation matrix
        correlation_matrix = final_df.corr()
        print(correlation_matrix)


        # Plot the heatmap
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

    elif selection == '11' or selection == 'q' : 
        # quit program 
        print("quitting")
        run = False

time.sleep(2)
sys.exit(0)