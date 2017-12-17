from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

def get_unique_venues():
	ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
	return ipl_df.venue.unique()

#Solution
