# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
import pandas as pd
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df(match_code):
    data = pd.DataFrame(ipl_df)
    df = data[data['match_code']== match_code]
    return (df)
   

get_match_specific_df(336018)

match_no = ipl_df['match_code']
type(match_no)

