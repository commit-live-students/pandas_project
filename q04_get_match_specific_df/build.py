import pandas as pd

def read_csv_data_to_df(path) :
    df=pd.read_csv(path)
    data=pd.DataFrame(df)
    return data
def get_match_specific_df(match_code):
    datas=read_csv_data_to_df('data/ipl_dataset.csv');
    output=datas.loc[(datas['match_code']==match_code)]
    #print(output)
    return output

print(get_match_specific_df(598057))


