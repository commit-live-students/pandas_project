
def get_runs_counts_by_match():
    return ipl_df.pivot_table(values='delivery', index='match_code', columns=['runs'], aggfunc='count')