import pandas as pd

def read_csv_data_to_df(path) :
    df=pd.read_csv(path,index_col=['match_code', 'runs'], 
        usecols=['match_code', 'runs'])
    data=pd.DataFrame(df)
    return data

def get_runs_counts_by_match():
    datas=read_csv_data_to_df('data/ipl_dataset.csv');
    #output=datas['runs']
    #output2=datas['match_code']
   # data1=pd.DataFrame(columns=datas['runs'],index=datas['match_code'])
    table = pd.pivot_table(datas, index=['match_code'],columns=['runs'],aggfunc=len)
    #print(table)
    return table

print(get_runs_counts_by_match())



