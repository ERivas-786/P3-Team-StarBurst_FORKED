import sys
import time
import Functions as fun


run = True
source_path = "Drew_folder\Drew_Data"
while(run) :

    selection = input("Enter selection (o for options): ")

    if selection.lower() == 'o' : 
        print(''' list of options: 
                1 - Choose datasets to compare
                (2) - print current paths
                3 - Create and print dataframes
                (4) - Print only dataframes
                5 - Create column names from dataframes
                (6) - Print all column names
                7 - Choose column names to analyze
                (8) - Convert datetime column to year only
                (9) - Print column names to analyze
                10 - Merge dataframes on chosen columns
                (11) - Print merged dataframe
                (12) - Group by chosen column
                13 - Generate and save correlation heatmap
                14 - Generate and save line graph
                15 - Or q to quit. ''')

    elif selection == "1" :
        fun.choose_datasets(source_path)

    elif selection == "2" : 
        fun.print_paths()

    elif selection == "3" :
        fun.create_and_print_dataframes()

    elif selection == "4" :
        fun.print_only_dataframes()

    elif selection == "5" :
        fun.create_column_names_from_dataframes()

    elif selection == "6" :
        fun.print_column_names_to_analyze_lists() 

    elif selection == "7" :
        fun.choose_column_names_to_analyze() 

    elif selection == "8" :
        fun.convert_datetime_column_to_year_only() 

    elif selection == "9" :
        fun.print_column_names_to_analyze() 

    elif selection == "10" :
        fun.merge_dataframes_on_chosen_columns() 

    elif selection == "11" :
        fun.print_merged_dataframe() 

    elif selection == "12" :
        fun.group_by_chosen_column() 

    elif selection == "13" :
        fun.new_school_heat_map() 

    elif selection == "14" :
        fun.generate_and_save_line_graph() 

    elif selection == '15' or selection == 'q' : 
        # quit program 
        print("quitting")
        run = False

time.sleep(2)
sys.exit(0)