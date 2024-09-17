import pandas as pd

def read_csv_data_to_df(path) :
    df=pd.read_csv(path)
    data=pd.DataFrame(df)
    return data

def get_unique_venues() :
    datas=read_csv_data_to_df('data/ipl_dataset.csv');
    return datas.venue.unique()

print(get_unique_venues())
    


