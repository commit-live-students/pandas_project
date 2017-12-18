from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("./data/ipl_dataset.csv")

def get_match_specific_df(match_code):
	if type(match_code) is int:
		return ipl_df[ipl_df['match_code']==match_code]
	else:
		return ipl_df[ipl_df['match_code']==int(match_code)]
