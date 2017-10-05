# Filter the data for a given `bowler`
If we ever wanted to access data for a particular bowler, we will have to first create a filter (a boolean series). Can you write that filter?

_Note:_ that you must return a boolean series (`Ture` if the condition is satisfied and `False` otherwise) filter, not the records that satisfy the filter.

## Wrtie a function `create_bowler_filter` that
- given a bowler's name, returns a boolian Series, which has `True` value for rows that contain the bowler's name in the "bowler" column, and `False` otherwise.

You can use previously created function (read_csv_data_to_df) to import csv into a dataframe.

## Parameters
- bowler: Name of the bowler `dtype: str`

## Returns
- filter: The filter to extract data `type: Series, dtype: bool`
