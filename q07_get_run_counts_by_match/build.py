# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    balls =[0,1,2,3,4,5,6]
    match_code = ipl_df['match_code']
    runs = ipl_df['runs']
    pivot_df = ipl_df.pivot_table(
                 values = 'runs',
                 index = 'match_code',
                 columns = ipl_df['runs'],
                 aggfunc='count')
    return pivot_df
get_runs_counts_by_match()
