import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q02_get_unique_values.build import get_unique_venues
<<<<<<< HEAD
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
=======
from greyatomlib.pandas.q01_read_csv_data_to_df.build import read_csv_data_to_df
>>>>>>> eed8c8c156e5093efb39cedf06b4c16d588a311f
from unittest import TestCase


class TestGet_unique_venues(TestCase):
    def test_get_unique_venues(self):
        path = "./data/ipl_dataset.csv"
        ipl_df = read_csv_data_to_df(path)
        venues = get_unique_venues()

        self.assertTrue(35 == len(venues))
