import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
import numpy as np
from q04_get_match_specific_df.build import get_match_specific_df
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
from unittest import TestCase

class TestGet_match_specific_df(TestCase):
    def test_get_match_specific_df(self):
        path = "./data/ipl_dataset.csv"
        ipl_df = read_csv_data_to_df(path)
        match_code = 598057
        expected_shape = (241,24)
        actual_shape = get_match_specific_df(match_code).shape
        self.assertTrue(expected_shape == actual_shape)
