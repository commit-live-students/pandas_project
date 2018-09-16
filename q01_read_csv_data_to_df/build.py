import pandas as pd

def read_csv_data_to_df(path) :
    df=pd.read_csv(path)
    data=pd.DataFrame(df)
    return data

print(read_csv_data_to_df('data/ipl_dataset.csv'))




