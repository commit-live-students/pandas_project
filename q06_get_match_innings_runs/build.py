# Default Imports
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")

# Solution
def get_match_innings_runs():
    run_series=ipl_df.groupby(['match_code','inning'])['runs'].sum()
    run_df=pd.DataFrame(run_series)
    return run_df
