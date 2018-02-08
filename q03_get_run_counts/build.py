# Default Imports
import pandas as pd
from pandas import Series,DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_run_counts():
    df = DataFrame(ipl_df)
    df1 =  df['runs']
    #df11 = df1.unique()
    df22 = df1.value_counts()
    s = Series(df22)
    runs_count = s.sort_index(ascending = True)
    #print type(runs_count)

    return runs_count


#print get_run_counts()
