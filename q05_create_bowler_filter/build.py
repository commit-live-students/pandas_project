# %load q05_create_bowler_filter/build.py
# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def create_bowler_filter(some_value):
    df=ipl_df
    l=df['bowler'] == some_value
    return l
df=ipl_df
some_value='I Sharma'
l=[df['bowler'] == some_value]

import pandas as pd
s=pd.Series([l])
s.head()
pd.Series([l]).cumsum()
l=[df['bowler'] == 'I Sharma']

pd.Series(l)


