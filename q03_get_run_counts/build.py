# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
import pandas as pd

def get_runs_counts():

    d2 = pd.DataFrame(ipl_df['runs'])
    runs_count = d2['runs'].value_counts()
    return runs_count

get_runs_counts()
