import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas

class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df(self):
        path = "../data/ipl_dataset.csv"
        df = read_csv_data_to_df(path)

        self.assertIsInstance(df, pandas.DataFrame)
        self.assertTrue(df.shape == (136522, 24))
