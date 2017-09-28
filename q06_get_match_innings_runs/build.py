
def get_match_innings_runs():
    return ipl_df[['match_code', 'inning', 'runs']].groupby(['match_code', 'inning']).sum()