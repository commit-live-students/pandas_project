import pandas as pd
import numpy as np

str_path='data/ipl_dataset.csv'

def read_csv_data_to_df(path):
	pd_df= pd.read_csv(path,  delimiter=',' )
	return pd_df

def get_unique_venues():
	npArray = np.array (df['venue'].unique())
	return npArray
	
	
df=read_csv_data_to_df(str_path)
print (df.shape)
npArray_Venues = get_unique_venues()
print (type(npArray_Venues))


