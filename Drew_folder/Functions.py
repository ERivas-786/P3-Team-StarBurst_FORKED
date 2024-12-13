import os
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

global path_1
global path_2
global df_1
global df_2
global df_1_truncated
global df_2_truncated
global df_merged
global final_df
global column_names_list_1
global column_names_list_2
global column_1
global column_1_1
global column_2
global column_2_2
file_save_path = "./Drew_folder/Drew_figures/"

def print_all_files(source_path):
    # Scan the directory and get
    # an iterator of os.DirEntry objects
    # corresponding to entries in it
    obj = os.scandir()

    # List all files and directories in the specified path
    # print("Files and Directories in '% s':" % source_path)
    dir_list = []
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            dir_list.append(entry.name)
    print(*dir_list, sep='\n')



def print_and_return_all_files_second_method(source_path):
   
    dir_list = os.listdir(source_path)
    print("Files and directories in '", source_path, "' :")
    # prints all files
    print(dir_list)
    return dir_list



def print_and_return_all_files_innumerated(source_path):
   
    dir_list = os.listdir(source_path)
    print("Files and directories in '", source_path, "' :")
    # prints all files
    for file in dir_list:
        print(str(dir_list.index(file)) + "-" + file)
    return dir_list



def choose_datasets(source_path):
    global path_1
    global path_2
    print('''Which datasets would you like to compare?
              Enter number of index for dataset 1 first,
              followed by index for dataset 2. ''')
    dir_list = print_and_return_all_files_innumerated(source_path)
    path_1 = "./Drew_folder/Drew_Data/" + dir_list[int(input())]
    path_2 = "./Drew_folder/Drew_Data/" + dir_list[int(input())]
    return path_1, path_2

def print_paths():
    print("The paths are: ")
    print("Path 1: " + path_1)
    print("Path 2: " + path_2)


def create_and_print_dataframes():
    global path_1
    global path_2
    global df_1
    global df_2

    df_1 = pd.read_csv(path_1)
    df_2 = pd.read_csv(path_2)

    print("The Dataframes are: ")
    print(path_1 + ":")
    print(df_1)
    print(path_2 + ":")
    print(df_2)



def create_column_names_from_dataframes():
    global df_1
    global df_2
    global column_names_list_1
    global column_names_list_2

    column_names_list_1 = list(df_1.columns.tolist())
    column_names_list_2 = list(df_2.columns.tolist())

    print("List of column names created! \n")

    return column_names_list_1, column_names_list_2

def print_only_dataframes():
    global df_1
    global df_2
    global path_1
    global path_2

    print(
f'''
    The dataframes are: 
    {path_1}
    {df_1}

    {path_2}
    {df_2}
    ''')


def choose_column_names_to_analyze():
    global column_names_list_1
    global column_names_list_2
    global column_1
    global column_1_1
    global column_2
    global column_2_2

    create_column_names_from_dataframes()

    print("The options for the first dataframe are: \n")
    for name in column_names_list_1:
        print(str(column_names_list_1.index(name)) + "- " + name)
    column_1 = column_names_list_1[int(input("Which column would you like to join in table 1? (number of index): "))]
    column_1_1 = column_names_list_1[int(input("Which column would you like to join in table 1? (number of index): "))]

    print("The options for the second dataframe are: \n")
    for name in column_names_list_2:
        print(str(column_names_list_2.index(name)) + "- " + name)
    column_2 = column_names_list_2[int(input("Which first column would you like to join in table 2? (number of index): "))]
    column_2_2 = column_names_list_2[int(input("Which second column would you like to join in table 2? (number of index): "))]
    return column_1, column_1_1, column_2, column_2_2


def print_column_names_to_analyze_lists():
    global column_names_list_1
    global column_names_list_2

    print("The columns in dataframe 1 are: \n")
    for name in column_names_list_1:
        print(str(column_names_list_1.index(name)) + "- " + name)

    print("\n")

    print("The columns in dataframe 2 are: \n")
    for name in column_names_list_2:
        print(str(column_names_list_2.index(name)) + "- " + name)

    print("\n")

def print_column_names_to_analyze():
    global column_1
    global column_1_1
    global column_2
    global column_2_2

    print(
    f'''The current columns to analyze are:
    {column_1}
    {column_1_1}
    {column_2}
    {column_2_2}
    ''')

def convert_datetime_column_to_year_only():
    global df_1
    global df_2

    print_column_names_to_analyze()

    which_dataframe = int(input("Which dataframe is the column in? (1, or 2): "))
    date = input("Which datetime column needs converted? (type it out): ")
    if which_dataframe == 1:

        # df_1['Year'] = df_1[date].dt.strftime('%Y')
        df_1[date] = pd.to_datetime(df_1[date])
        df_1['Year'] = df_1[date].dt.year
        print(df_1)
    if which_dataframe == 2:
        df_1[date] = pd.to_datetime(df_1[date])
        df_2['year'] = df_2[date].dt.year


def merge_dataframes_on_chosen_columns():
    global df_1
    global df_2
    global final_df
    global column_1
    global column_1_1
    global column_2
    global column_2_2
    
    

    print('''
    Columns to be merged on
    (with same data)
    need to be renamed to the same name to be merged properly. ''')
    print("The column names are now: \n Dataframe 1: " + column_1 + ", " + column_1_1 + "\n Dataframe 2: " + column_2 + ", " + column_2_2 + "\n")
    
    renaming = input("Should any columns be renamed? (y or n) ")
    while renaming == "y":
        df_number = int(input("Which dataframe is the column in? (1 or 2): "))
        column_number = int(input("Which column should be renamed? (1 or 2): "))

        if df_number == 1:

            if column_number == 1:
                new_name = input("What should the new name be?: ")
                df_1 = df_1.rename(columns={column_1: new_name})
                column_1 = new_name
                print("The column names are now: \n Dataframe 1: " + column_1 + " " + column_1_1 + "\n Dataframe 2: " + column_2 + " " + column_2_2 + "\n")
                renaming = input("Would you like to continue renaming? (y or n): ")


            elif column_number == 2:
                new_name = input("What should the new name be?: ")
                df_1 = df_1.rename(columns={column_1_1: new_name})
                column_1_1 = new_name
                print("The column names are now: \n Dataframe 1: " + column_1 + " " + column_1_1 + "\n Dataframe 2: " + column_2 + " " + column_2_2 + "\n")
                renaming = input("Would you like to continue renaming? (y or n): ")

        elif df_number == 2:
            
            if column_number == 1:
                new_name = input("What should the new name be?: ")
                df_2 = df_2.rename(columns={column_2: new_name})
                column_2 = new_name
                print("The column names are now: \n Dataframe 1: " + column_1 + " " + column_1_1 + "\n Dataframe 2: " + column_2 + " " + column_2_2 + "\n")
                renaming = input("Would you like to continue renaming? (y or n): ")

            elif column_number == 2:
                new_name = input("What should the new name be?: ")
                df_2 = df_2.rename(columns={column_2_2: new_name})
                column_2_2 = new_name
                print("The column names are now: \n Dataframe 1: " + column_1 + " " + column_1_1 + "\n Dataframe 2: " + column_2 + " " + column_2_2 + "\n")
                renaming = input("Would you like to continue renaming? (y or n): ")

        else:
            print("Enter only 1 or 2. ")
        
    merge_column = ""
    if (column_1 == column_2):
        merge_column = column_1
        df_merged = pd.merge(df_1, df_2, on = merge_column)
        final_df = df_merged[[column_1_1, merge_column, column_2_2]]
        final_df.dropna()
        final_df.reindex(axis = 0)
        print("\n Dataframes successfully merged! \n")

    elif (column_1 == column_2_2):
        merge_column = column_1_1
        df_merged = pd.merge(df_1, df_2, on = merge_column)
        final_df = df_merged[[column_1_1, merge_column, column_2]]
        final_df.dropna()
        final_df.reindex(axis = 0)
        print("\n Dataframes successfully merged! \n")

    elif (column_1_1 == column_2):
        merge_column = column_1_1
        df_merged = pd.merge(df_1, df_2, on = merge_column)
        final_df = df_merged[[column_1, merge_column, column_2_2]]
        final_df.dropna()
        final_df.reindex(axis = 0)
        print("\n Dataframes successfully merged! \n")

    elif (column_1_1 == column_2_2):
        merge_column = column_1_1
        df_merged = pd.merge(df_1, df_2, on = merge_column)
        final_df = df_merged[[column_1, merge_column, column_2]]
        final_df.dropna()
        final_df.reindex(axis = 0)
        print("\n Dataframes successfully merged! \n")

    else:
        print("Columns don't match. Can't merge. ")

def group_by_chosen_column():
    global final_df

    print("The column names are: \n Final Dataframe: 0- " + final_df.columns[0]+ ", 1- " + final_df.columns[1]+ ", 2- " + final_df.columns[2])
    group_by_column = input("Which column would you like to group by? (type it out): ")
    final_df = final_df.groupby(group_by_column).mean().reset_index()

def new_school_heat_map():
    global final_df

    correlation_matrix = final_df.corr()
    print(correlation_matrix)
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")

    # save = input("Would you like to save the heatmap? (y or n) ")
    # if save == "y":
    heatmap_name = input("What would you like to call the heatmap? ")
    plt.savefig(file_save_path + heatmap_name)
    plt.show()

def generate_and_save_line_graph():
    global final_df

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the first column on the primary y-axis
    final_df.plot(x=final_df.columns[0], y=final_df.columns[1], ax=ax1)

    # Create a secondary y-axis
    ax2 = ax1.twinx()

    # Plot the second column on the secondary y-axis
    final_df.plot(x=final_df.columns[0], y=final_df.columns[2], ax=ax2, color='red')

    # Set the y-axis scales

    print(
    f'''
    The datasets are:
        {final_df.columns[1]}
        {final_df.columns[2]}''')
    axis_1_scale = input('''
    Which scale should the first dataset have? 
        (linear: Linear scale (default)
        log, 
        symlog, 
        logit: Logit scale (for values between 0 and 1))
        ''')
    axis_2_scale = input("Which scale should the second dataset have? (type it out): ")
    ax1.set_yscale(axis_1_scale) 
    ax2.set_yscale(axis_2_scale)    

    # Set y-axis labels
    ax1.set_ylabel(final_df.columns[1])
    ax2.set_ylabel(final_df.columns[2])

    plt.title(final_df.columns[1] + " vs " + final_df.columns[2] + " by " + final_df.columns[0])
    fig.tight_layout()
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # plt.show()

    # save = input("Would you like to save the heatmap? (y or n) ")
    # if save == "y":
    line_graph_name = input("What would you like to call the line graph?: ")
    plt.savefig(file_save_path + line_graph_name)
    plt.show()

def print_merged_dataframe():
    global final_df
    print(final_df)
    