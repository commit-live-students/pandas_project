# Count of runs per match

Whoa!! That was too much work and you did great!

CONGRATULATIONS!!

Now, let's get ready for the final hurdle!!

In a previous question, we calculated the counts of runs to understand which of those are scored the most. Now, we wish to see if this distribution is followed in all matches, so we can find "outlier" matches: those with unusually good/bad bowling/batting.

So what we want is a dataframe with
* match_code as the row index (rows)
* 0, 1,...6 runs (scored by batsman) as columns
* count of such deliveries as the aggregated values of the dataframe

Use the pivot_table method to achieve this.

Cmon, let's do it.

Create a function that answers this question.
The function should :

* Be named get_runs_counts_by_match
* Accept no parameters
* Work on the previously created ipl_df object
* Should return a dataframe with 3 columns: match_code, inning, runs

_HINTS_ : 

* When calling the pivot_table() function, you can simply pass the string 'count' to the parameter aggfunc to use count as aggregator
* Do not call reset_index() on the dataframe returned from the pivot table.
