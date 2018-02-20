# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
path = "./data/ipl_dataset.csv""
# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

print read_csv_data_to_df(path)

'''def get_unique_venues():
    venues = ipl_df['venue'].unique()
    return venues'''
