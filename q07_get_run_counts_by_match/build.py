# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():

    x = ipl_df.pivot_table(index=["match_code"],columns=["runs"],fill_value=0,aggfunc="count")
    #print x
    
    return x["batsman"]
