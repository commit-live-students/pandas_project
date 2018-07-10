from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

match_code = 598057
def get_match_specific_df(match_code):
    count = ipl_df[ipl_df['match_code'] == match_code ]
    return count

get_match_specific_df(match_code)
