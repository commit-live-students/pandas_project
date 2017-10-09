# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

def read_csv_data_to_df(path) :
    #path = path
    a = pd.read_csv(path)
    #print a
    return a

# Solution
