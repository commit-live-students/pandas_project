import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
import numpy as np
from q04_get_match_specific_df.build import get_match_specific_df
from q01_read_csv_data_to_df.build import read_csv_data_to_df
from unittest import TestCase

class TestGet_match_specific_df(TestCase):
    def test_get_match_specific_df(self):
        path = "../data/ipl_dataset.csv"
        ipl_df = read_csv_data_to_df(path)
        match_code = 598057
        expected = (ipl_df[ipl_df['match_code'] == match_code])
        actual = get_match_specific_df(match_code)
        self.assertTrue(expected.shape == actual.shape)
