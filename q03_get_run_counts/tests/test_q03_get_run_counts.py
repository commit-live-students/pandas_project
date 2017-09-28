import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
import numpy as np
from q03_get_run_counts.build import get_run_counts
from q01_read_csv_data_to_df.build import read_csv_data_to_df
from unittest import TestCase

class TestGet_run_counts(TestCase):
    def test_get_run_counts(self):
        path = "../data/ipl_dataset.csv"
        ipl_df = read_csv_data_to_df(path)
        actual =  get_run_counts()
        expected = ipl_df['runs'].value_counts()
        self.assertTrue(np.all(expected == actual))
