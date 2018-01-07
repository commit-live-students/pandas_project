from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def create_bowler_filter(baller):
    a= ipl_df['bowler']
    expected_filter = (a == baller)
    return expected_filter
