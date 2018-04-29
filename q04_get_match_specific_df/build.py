import pandas as pd

def get_match_specific_df(match_code):
    ipl_data=pd.read_csv('./data/ipl_dataset.csv')
    ans=ipl_data[ipl_data['match_code']==match_code]
    return ans
ans=get_match_specific_df(598057)
ans

