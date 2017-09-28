import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
import numpy as np
from q06_get_match_innings_runs.build import get_match_innings_runs
from q01_read_csv_data_to_df.build import read_csv_data_to_df
from unittest import TestCase


class TestGet_match_innings_runs(TestCase):
    def test_get_match_innings_runs(self):
        path = "../data/ipl_dataset.csv"
        ipl_df = read_csv_data_to_df(path)
        bowler = 'I Sharma'
        expected = ipl_df[['match_code', 'inning', 'runs']].groupby(['match_code', 'inning']).sum()
        actual = get_match_innings_runs()

        self.assertTrue(np.all(expected == actual))
