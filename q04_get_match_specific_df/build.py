# Default imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

def get_match_specific_df(matchcode):
    # You have been given dataset already in 'ipl_df'.
    code = int(matchcode)
    ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")
    df = ipl_df[ipl_df['match_code'] == code]
    return df
