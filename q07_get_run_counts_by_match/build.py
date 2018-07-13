
import pandas as pd
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

def get_runs_counts_by_match():
    ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
    df1 = pd.DataFrame(ipl_df[['match_code','runs','venue']])
    df2 = df1.groupby(['match_code','runs'], as_index=False).count()
    df = df2.pivot(index='match_code',columns='runs')
    df = df.fillna(0)
    df = df.astype('int')
    return df

get_runs_counts_by_match()
