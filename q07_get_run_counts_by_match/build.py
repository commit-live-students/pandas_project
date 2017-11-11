# Default Imports
#from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = pd.read_csv("/home/darshind/Workspace/code/pandas_project/data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    df = ipl_df.pivot_table(values = 'bowler',columns = 'runs',index ='match_code',aggfunc='count')
    #filter_data = [['match_code','runs','inning']]
    return df
#get_runs_counts_by_match()
