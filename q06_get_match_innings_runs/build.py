# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

def get_match_innings_runs():
    ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
    runs = ipl_df[['match_code','inning','runs']]
    return runs.groupby(by=('match_code','inning') ).sum()
