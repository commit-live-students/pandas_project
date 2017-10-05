# Default Imports
<<<<<<< HEAD
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
=======
from greyatomlib.pandas.q01_read_csv_data_to_df.build import read_csv_data_to_df
>>>>>>> eed8c8c156e5093efb39cedf06b4c16d588a311f

# You have been give the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
<<<<<<< HEAD
=======
def get_runs_counts_by_match():
    runs_by_match = ipl_df.pivot_table(values='delivery', index='match_code', columns=['runs'],
                                       aggfunc='count')
    return runs_by_match
>>>>>>> eed8c8c156e5093efb39cedf06b4c16d588a311f
