# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
    ipl_df['count'] = 1
    pt = ipl_df.pivot_table(values = 'count',index = 'match_code',columns = 'runs', aggfunc=sum)
    return pt
