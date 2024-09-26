from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def get_run_counts():
    runs_count = ipl_df['runs'].value_counts()
    return runs_count.sort_index()




