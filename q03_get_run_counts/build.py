import pandas as pd
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
from pandas import Series, DataFrame
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    ipl_df1 = pd.DataFrame(ipl_df)
    scored = ipl_df1.groupby('runs')
    score_count = scored['runs'].count()
    return score_count

print get_run_counts()
