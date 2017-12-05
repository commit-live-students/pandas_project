# Default Imports
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

# Path has been given to you already to use in function.
path = "data/ipl_dataset.csv"

def read_csv_data_to_df(path):
    return DataFrame(pd.read_csv(path))

print read_csv_data_to_df(path)
