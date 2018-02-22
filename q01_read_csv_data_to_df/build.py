# Default Imports
import pandas as pd
from pandas import Series, DataFrame

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

# Solution
def read_csv_data_to_df(path):
    df_ipl = pd.read_csv(path)
    return df_ipl

df1 = read_csv_data_to_df(path)
print df1.shape
