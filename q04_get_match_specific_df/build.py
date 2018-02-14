from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_match_specific_df(match):

    unique_match_count = ipl_df.match_code.value_counts()
    match_length = unique_match_count[int(match)]
    match_data = ipl_df.iloc[0:match_length,:]

    return match_data
