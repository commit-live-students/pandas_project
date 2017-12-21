# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
    ipl_df2 =ipl_df.groupby(['runs'])['match_code'].count()
    return ipl_df2
