# Count of runs per match

Whoa!! That was a lot of work and you did great!

CONGRATULATIONS!!

Now, let's get ready for the final hurdle!!

In a previous question, we calculated the counts of runs to understand which of those are scored the most. Now, we wish to see if this distribution is followed in all matches, so we can find "outlier" matches: those with unusually good/bad bowling/batting.

## Write a function `get_runs_counts_by_match` that

* Has
  * match_code as the row index (rows)
  * 0, 1,...6 runs (scored by batsman) as columns
  * count of frequency as the aggregated values of the dataframe
* You can use the `pivot_table` method to achieve this.
* You can use previously created function (read_csv_data_to_df) to import csv into a dataframe.

### PARAMETERS 
No parameters

### RETURNS
- df: Pivot table with match_code as index, runs columns and frequency as values. `type: DataFrame`

_**HINTS**_ : 

* When calling the pivot_table() function, you can simply pass the string 'count' to the parameter aggfunc to use count as aggregator
* Do not call reset_index() on the dataframe returned from the pivot table.
