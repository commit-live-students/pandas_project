# Default Imports
import pandas as pd

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"
path1 = "data/ipl_dataset.csv"
path2 = "data/weather_2012.csv"
def read_csv_data_to_df(path):
	return pd.read_csv(path)
