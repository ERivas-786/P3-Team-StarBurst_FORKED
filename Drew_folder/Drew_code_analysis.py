import os
import sys
import time
import Functions as fun
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


run = True
source_path = "Drew_folder\Drew_Data"
while(run) :

    selection = input("Enter selection (o for options): ")

    if selection.lower() == 'o' : 
        print(''' list of options: 
                1 - Choose datasets to compare
                (2) - print current paths
                3 - Create and print dataframes
                4 - Create column names from dataframes
                (5) - Print column names to analyze
                6 - Choose column names to analyze
                (7) - Print column names to analyze
                8 - Merge dataframes on chosen columns
                (9) - Print merged dataframe
                10 - Generate correlation heatmap
                11 - Or q to quit. ''')

    elif selection == "1" :
        fun.choose_datasets(source_path)

    elif selection == "2" : 
        fun.print_paths()

    elif selection == "3" :
        fun.create_and_print_dataframes()

    elif selection == "4" :
        fun.create_column_names_from_dataframes()

    elif selection == "5" :
        fun.print_column_names_to_analyze_lists() 

    elif selection == "6" :
        fun.choose_column_names_to_analyze() 

    elif selection == "7" :
        fun.print_column_names_to_analyze() 

    elif selection == "8" :
        fun.merge_dataframes_on_chosen_columns() 

    elif selection == "9" :
        fun.print_merged_dataframe() 

    elif selection == "10" :
        fun.new_school_heat_map() 

    elif selection == '11' or selection == 'q' : 
        # quit program 
        print("quitting")
        run = False

time.sleep(2)
sys.exit(0)