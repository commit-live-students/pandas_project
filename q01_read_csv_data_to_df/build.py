import pandas as pd
import numpy as np

str_path='data/ipl_dataset.csv'

def read_csv_data_to_df(path):
	pd_df= pd.read_csv(path,  delimiter=',' )
	return pd_df



df=read_csv_data_to_df(str_path)
print (df.shape)



