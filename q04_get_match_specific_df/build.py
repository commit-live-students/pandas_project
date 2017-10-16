# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_match_specific_df(match_code):
    #path = "./data/ipl_dataset.csv"
    #ipl_df = read_csv_data_to_df(path)
    #print ipl_df.loc[match_code,'match_code'].head()
    return ipl_df[ipl_df['match_code'] == match_code]
