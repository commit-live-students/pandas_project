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


def create_bowler_filter(strBowler):
	series_Bowler = pd.Series(df['bowler'].str.contains(strBowler) == True)
	print(series_Bowler.sum())


def get_match_innings_runs():
	dfGrp_runs = df.groupby(['match_code','inning'])
	#.agg(np.sum)
	#print (dfGrp_runs)
	#print (dfGrp_runs['runs'].agg(np.sum))
	return dfGrp_runs['runs'].agg(np.sum)

def get_runs_counts_by_match():
	pivot_df = df.pivot_table(
					values='total',      # We want to aggregate the values of which column?
					index=['match_code'],       # We want to use which column as the new index?
					columns=['runs'],   # We want to use the values of which column as the new columns? (optional)
					aggfunc=(np.max),
					fill_value='-')
					#.loc[['SR Tendulkar','DR Smith']] 
	return pivot_df

df=read_csv_data_to_df(str_path)
#print (df.shape)
#npArray_Venues = get_unique_venues()
#print (type(npArray_Venues))
#srs_run_counts = get_run_counts()
#get_match_specific_df(598057)
#create_bowler_filter('I Sharma')
get_match_innings_runs()
get_runs_counts_by_match()


