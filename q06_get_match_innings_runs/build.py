import pandas as pd

def read_csv_data_to_df(path) :
    df=pd.read_csv(path)
    data=pd.DataFrame(df)
    return data

def get_match_innings_runs():
    datas=read_csv_data_to_df('data/ipl_dataset.csv');
    output=datas.groupby('inning').sum()['runs']
   # print(output)
    return output.sum()

print(get_match_innings_runs())



