import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
import numpy as np
from q05_create_bowler_filter.build import create_bowler_filter
from q01_read_csv_data_to_df.build import read_csv_data_to_df
from unittest import TestCase


class TestCreate_bowler_filter(TestCase):
    def test_create_bowler_filter(self):
        path = "../data/ipl_dataset.csv"
        ipl_df = read_csv_data_to_df(path)
        bowler = 'I Sharma'
        expected = (ipl_df['bowler'] == bowler)
        actual = create_bowler_filter(bowler)
        self.assertTrue(np.all(expected == actual))
