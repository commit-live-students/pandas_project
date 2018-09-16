import pandas as pd

def read_csv_data_to_df(path) :
    df=pd.read_csv(path)
    data=pd.DataFrame(df)
    return data

def get_run_counts() :
    datas=read_csv_data_to_df('data/ipl_dataset.csv');
    #df=datas.groupby('runs').count()
    
    return datas['runs'].value_counts()

print(get_run_counts())


