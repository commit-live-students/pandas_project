import pandas as pd
path = "data/ipl_dataset.csv"
def read_csv_data_to_df(path):
    reads = pd.read_csv(path)
    return reads
