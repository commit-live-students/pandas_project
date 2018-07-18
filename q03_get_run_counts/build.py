# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df


# You have been given the dataset already in 'ipl_df'.
def get_run_counts():
    ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
    run_counts = ipl_df['runs'].value_counts()
    return run_counts



# Solution
