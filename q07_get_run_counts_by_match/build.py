# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
def get_runs_counts_by_match():
    import pandas as pd
    ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')
    df=ipl_df[['match_code','runs']]
    tab= pd.pivot_table(df, index=['match_code'], values=['match_code'],columns=['runs'] , aggfunc=len)
    
    return tab
  
# Solution



