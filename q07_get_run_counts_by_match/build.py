# %load q07_get_run_counts_by_match/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_runs_counts_by_match():
    ipl_pivot=ipl_df.pivot_table(index='match_code',columns=['runs'],values='batsman',aggfunc='count')
    return ipl_pivot
    
import numpy as np
import pandas as pd
ipl_df.pivot_table(index='match_code',columns=['runs'],values='batsman',aggfunc='count')
ipl_df.head()



