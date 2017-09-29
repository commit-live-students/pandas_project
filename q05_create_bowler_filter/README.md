# Filter the data for a given `bowler`
If we ever wanted to access data for a particular bowler, we will have to first create
a filter (a boolean series) to filter the data. Can you write that filter?

Note that you must return a boolean series filter
not the records that satisfy the filter

Create a function `create_bowler_filter` 
Work on the previously created `ipl_df` object

## Parameters
- bowler: Name of the bowler `dtype: str`
## Returns
- filter: The filter to extract data `type: Series, dtype: bool`