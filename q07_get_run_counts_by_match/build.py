# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    ipl=ipl_df[['runs','match_code']]
    ipl['runs1']=ipl_df['runs']
    runcount = ipl.pivot_table(index=['match_code'],columns=['runs1'],aggfunc='count')
    return runcount
get_runs_counts_by_match()


