import pandas as pd

def read_csv_data_to_df(path) :
    df=pd.read_csv(path)
    data=pd.DataFrame(df)
    return data

def create_bowler_filter(name):
    datas=read_csv_data_to_df('data/ipl_dataset.csv');
    output=(datas['bowler']==name)
    #print(output)
    return output

print(create_bowler_filter('I Sharma'))


