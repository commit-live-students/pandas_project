from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given the dataset already in 'ipl_df'.
ipl_df_path = "data/ipl_dataset.csv"
s= set()
#Solution
def get_unique_venues():
    df = pd.read_csv(ipl_df_path)
    venues = df['city'].unique()
    return venues
