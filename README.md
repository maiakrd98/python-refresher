# python-refresher
`my_utils.py` contains the function `get_column()`, which takes in a file name, query column, query value, and optionally a result column (which defaults to 1). It opens the file and returns the values in the results column for which the value of the query column matches the query value.

`print_fires.py` uses `get_column()` to print the emmissions due to fires in Canada for each year between 1990 and 2020 based on the data in `Agrofood_co2_emission.csv`.