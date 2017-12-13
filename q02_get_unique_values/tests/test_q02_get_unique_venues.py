import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q02_get_unique_values.build import get_unique_venues
from inspect import getargspec
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
from unittest import TestCase

path = "./data/ipl_dataset.csv"
ipl_df = read_csv_data_to_df(path)
venues = get_unique_venues()

class TestGet_unique_venues(TestCase):
    
    def test_get_unique_venues_count(self):
        self.assertEqual(35 , len(venues),"The Expected values do not match with the returned value")
