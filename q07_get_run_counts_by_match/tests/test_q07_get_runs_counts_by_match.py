import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
import numpy as np
from q07_get_run_counts_by_match.build import get_runs_counts_by_match
from greyatomlib.pandas.q01_read_csv_data_to_df.build import read_csv_data_to_df
from unittest import TestCase

class TestGet_runs_counts_by_match(TestCase):
    def test_get_runs_counts_by_match(self):
        path = "./data/ipl_dataset.csv"
        ipl_df = read_csv_data_to_df(path)
        bowler = 'I Sharma'
        expected = (577,7)
        actual = get_runs_counts_by_match()
        self.assertTrue(actual.shape == expected)