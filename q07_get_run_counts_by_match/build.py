from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_runs_counts_by_match():
# Solution
    pivot_df = ipl_df.pivot_table(
                values='date',      # We want to aggregate the values of which column?
                index='match_code',       # We want to use which column as the new index?
                columns=['runs'],   # We want to use the values of which column as the new columns? (optional)
                aggfunc='count')  # What aggregation function to use ?
    return pivot_df
