# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_runs_counts_by_match():
  ##  return ipl_df.info()

    pivot_df = ipl_df.pivot_table(
        values='total',      # We want to aggregate the values of which column?
        index='match_code',       # We want to use which column as the new index?
        columns=['runs'],   # We want to use the values of which column as the new columns? (optional)
        aggfunc=len)  # What aggregation function to use ?

# Notice that the result is a hierarchical index
    return pivot_df
