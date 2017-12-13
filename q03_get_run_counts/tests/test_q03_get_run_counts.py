import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
import numpy as np
from q03_get_run_counts.build import get_run_counts
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
from unittest import TestCase
path = "./data/ipl_dataset.csv"
ipl_df = read_csv_data_to_df(path)
result =  get_run_counts()
class TestGet_run_counts(TestCase):
    def test_get_run_counts_return_value_5(self):
        
        self.assertEqual(result[5],42,"The return value does not match the expected value")
    def test_get_run_counts_return_values_6(self):
        self.assertEqual(result[6] , 5806,"The return value does not match the expected value")

    def test_get_run_counts_return_values_shape(self):
        self.assertEqual(result.shape , (7,), "The shape does not match with the expected shape")
