import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
path = "./data/ipl_dataset.csv"
ipl_df = read_csv_data_to_df(path)
def get_run_counts():
    runs_count=pd.Series.value_counts(ipl_df['runs'])
    return runs_count
