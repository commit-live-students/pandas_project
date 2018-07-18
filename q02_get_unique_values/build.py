import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
def get_unique_venues():
	return pd.unique(ipl_df['venue'])
