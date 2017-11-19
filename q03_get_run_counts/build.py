# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
from pandas import Series
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    a = ipl_df['runs']
    b = a.unique()
    runs_counts = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}

    for i,j in enumerate(a):
        runs_counts[j] += 1
    result = Series(runs_counts)
    return result
