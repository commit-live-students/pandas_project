
def get_match_specific_df(match_code):
    return ipl_df[ipl_df['match_code'] == match_code]