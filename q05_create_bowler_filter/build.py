from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
import numpy as np

ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

def create_bowler_filter(player_name):
    check_bowler = ipl_df['bowler'] == player_name
    
    return check_bowler



