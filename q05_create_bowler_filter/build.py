# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
import pandas as pd
def create_bowler_filter(bowler) :
    #path = path
    a = pd.read_csv("data/ipl_dataset.csv")
    df = a[(a.bowler == bowler)]
    filter = (a['bowler'] == bowler)
    #print a
    return filter
# Solution
