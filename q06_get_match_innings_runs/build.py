# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
import numpy as np

ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
import numpy as np
import pandas as pd
def get_match_innings_runs():

    df1 = ipl_df["runs"].groupby([ipl_df.match_code,ipl_df.inning]).agg(np.sum)
    df2 = pd.DataFrame(df1)
    return df2


get_match_innings_runs()
