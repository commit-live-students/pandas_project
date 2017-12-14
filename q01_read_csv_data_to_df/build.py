
import pandas as pd
from pandas import Series, DataFrame

path = "data/ipl_dataset.csv"

def read_csv_data_to_df (path):
    #df_ipl_data = DataFrame.from_csv(path)
    df_ipl_data = pd.read_csv(path)
    return df_ipl_data
