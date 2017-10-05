# Data related to a particular match
We will give you a match code and you will have to give us the data for that match. 

Up for it?

## Create a function `get_match_specific_df` that
- returns data for a given match code

You can use previously created function (`read_csv_data_to_df`) to import csv into a dataframe.

### Parameters
- match_code: The code of the match. `dtype:int`

### Returns
- df: The data of the match `dtype: DataFrame`

_Brain Teaser_: 
1. It might be worth checking the data type of `match_code` columns. Depending on what you find, you can change the `dtype` of the input parameter. 
2. Would that fact make any difference to your final solution?
