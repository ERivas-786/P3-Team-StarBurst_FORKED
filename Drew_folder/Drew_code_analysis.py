import os
import sys
import time
import Functions as fun
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


run = True
source_path = "Drew_folder"
while(run) :

    selection = input("Enter selection (o for options): ")

    if selection.lower() == 'o' : 
        print(''' list of options: 
                1 - Choose datasets to compare
                2 - Print current working datasets
                3 - Create and print dataframes
                4 - Display column names in each dataset
                5 - Chose columns to compare
                6 - Print correlation matrix for chosen columns
                7 - Or q to quit. ''')

    elif selection == "1" :
        fun.choose_datasets(source_path)

    elif selection == "2" : 
        fun.print_datasets()

    elif selection == "3" :
        fun.create_and_print_dataframes()

    elif selection == "4" :
        fun.List_all_files(source_path) 

    elif selection == "5" :
        fun.List_all_files(source_path) 

    elif selection == '6' or selection == 'q' : 
        # quit program 
        print("quitting")
        run = False

time.sleep(2)
sys.exit(0)