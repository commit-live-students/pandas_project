import pandas as pd
import numpy as np

str_path='data/ipl_dataset.csv'

def read_csv_data_to_df(path):
	pd_df= pd.read_csv(path,  delimiter=',' )
	return pd_df

def get_unique_venues():
	npArray = np.array (df['venue'].unique())
	return npArray
	
def get_run_counts():
	np_unqRunCount = np.array(df['runs'].value_counts()[df['runs'].unique()])
	np_unqRuns = np.array(df['runs'].unique())
	#print (np_unqRunCount)
	#print (np_unqRuns)
	print(' np_unqRunCount : ',np_unqRunCount[0:])
	series_run_counts = pd.Series(data = np_unqRunCount[0:], index=np_unqRuns)
	return series_run_counts


def get_match_specific_df(iMatchCode):
	df_MatchCode = df[df['match_code']==iMatchCode ]
	print(df_MatchCode.shape)
	return df_MatchCode

df=read_csv_data_to_df(str_path)
#print (df.shape)
npArray_Venues = get_unique_venues()
#print (type(npArray_Venues))
srs_run_counts = get_run_counts()
get_match_specific_df(598057)


