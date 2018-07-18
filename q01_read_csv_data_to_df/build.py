import pandas as pd

path = "data/ipl_dataset.csv"

# Path has been given to you already to use in function.
def read_csv_data_to_df(path):
    data = pd.read_csv(path)
    result = pd.DataFrame(data)
    return result
