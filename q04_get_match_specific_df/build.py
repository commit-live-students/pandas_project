from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df


# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

# Solution
def get_match_specific_df(match_code):
    if isinstance(match_code, int):
        df1 = ipl_df[ipl_df['match_code'] == match_code]
        return df1
    else:
        raise TypeError('Function accepts only integer argument, ''match_code'' passed {} is not an integer'.format(match_code))
