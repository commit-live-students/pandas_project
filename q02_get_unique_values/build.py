# %load q02_get_unique_values/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given the dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

path = 'data/ipl_dataset.csv'
#Solution
def read_csv_data_to_df(path):
    ipl_data = pd.read_csv(path)
    return ipl_data
    read_csv_data_to_df(path)



