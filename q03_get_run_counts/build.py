# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    pivot_tbl = ipl_df.pivot_table(
                values= 'runs', index=ipl_df['runs'], aggfunc=lambda x: len(x))
    return pivot_tbl['runs']
#print type(get_run_counts())
