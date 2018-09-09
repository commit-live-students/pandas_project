from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np

ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

def get_match_innings_runs():
    df = ipl_df.groupby(['match_code','inning',])['runs'].agg(np.sum)
    
    return df




from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np

ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')
df = ipl_df.groupby(['match_code','inning',])['runs'].agg(np.sum)
print(df)


