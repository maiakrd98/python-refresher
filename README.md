# Python Refresher
This repository contains code for reading a file containing data on greenhouse gas emissions from various sources and various countries and printing the emissions from a particular country and a particular source. It also contains code for calculating the mean, median, and standard deviation of a list of integers and to apply those operations to the emissions data.

## Installation and set up
First, open your Terminal and navigate to the directory that you want this repository to be located in. Then clone the repository by running
```
git clone https://github.com/maiakrd98/python-refresher.git
```

Next, navigate to the `python-refresher` folder by running 
```
cd python-refresher
```

Here, you will see all the files in the repository.

To set up the environment, first run this code to create the environment:
```
mamba env create -f environment.yml
```

Then activate the environment by running
```
mamba activate swe4s
```

This environment contains `pycodestyle` for checking that python code is compliant with the PEP 8 style guide and `wget` for running the functional test file.

## Data files
This repository expects a file called `Agrofood_co2_emission.csv`. This should be a comma separated file with countries listed in the first column, years listed in the second column, and corresponding greenhouse gas emmissions from various sources listed in the remaining columns.

This repository also contains a small data file called `Agrofood_co2_emissions_test_file.csv` in `test/func` that contains only a few countries, years, and emmision types and is used in testing.

## Usage examples

`print_fires.py` takes in four required command line inputs: `--file_name`, which is the name of the data file, `--country`, which is the country you are interested in, `--country_column`, which is the column that the countries are listed in, and `--fires_column`, which is the column where the fire emmissions (or other emmissions of interest) are listed. It also take in one optional command line input `--operation`, which specifies an operation (mean, median, or standard deviation) to perform. The only accepted values for `--operation` are `'mean'`, `'median'`, or `'sd'`. 

If no operation is supplied, `print_fires.py` uses the function `get_column()` in `my_utils.py` to open the file and return the values in the fires column for which the value of the country column matches the given country. It also converts those values to integers and prints them. If an operation is supplied, `print_fires.py` does not print the values from `get_column()`, but instead calculates their mean, median, or standard deviation and prints that.

For example, running
```
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'Canada' --country_column 0  --fires_column 3
```
from the main directory of the repository (`python-refresher`, unless you have named it something else) will print a vector of emmissions due to fires in Canada for each year between 1990 and 2020, since fire emmissions are listed in the fourth column of `Agrofood_co2_emission.csv`. Similarly, running 
```
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'Afghanistan' --country_column 0  --fires_column 17
```
will print a vector of emmissions due to fertilizer manufacturing in Afghanistan for each year between 1990 and 2020, since fertilizer manufacturing emmissions are listed in the eighteenth column of `Agrofood_co2_emission.csv`.

The following examples use the operation argument as well.
```
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'Canada' --country_column 0  --fires_column 3 --operation 'mean'
```
will print the mean emmissions due to fires in Canada for between 1990 and 2020 and
```
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'Afghanistan' --country_column 0  --fires_column 17 --operation 'sd'
```
will print the standard deviation of emmissions due to fertilizer manufacturing in Afghanistan between 1990 and 2020.

You can also run several examples using `run.sh` as follows:
```
./run.sh
```
This will perform one successful run, one run that gives an error due to a typo in the file name, and one run that gives an error because one of the column numbers is too large/out of bounds.

To check that the python files follow the PEP 8 style guide, run
```
pycodestyle print_fires.py my_utils.py test/unit/test_my_utils.py
```

## Testing instructions

To run the functional tests, which check that `print_fires.py` is working properly, navigate to the functional test directory (`test/func`):
```
cd test/func
```
and run the following command
```
bash test_print_fires.sh
```
You should see that 28 tests have run with hopefully 28 successes.

To run the unit tests from the main directory of the repository, run the following command
```
python -m unittest discover -s test/unit
```
You should see that it ran 29 tests and says OK at the bottom. You will see some error messages interspersed with the dots that represent successful tests, but you can ignore those - they are just from the tests that are checking that errors are raised when they should be. 

## Update history

### v1.0
- Initial project
- Implement `get_columns()`
- Use `get_columns()` to print Canadian fire emissions in `print_fires.py`
- One example in `run.sh`

### v2.0.0
- Implement command line arguments for `print_fires.py`
- Handle errors
- Add failure examples to `run.sh`
- Ensure best practices

### v3.0
- Implement mean, median, and standard deviation functions
- Add optional operation argument to `print_fires.py`
- Add unit tests for all functions in `my_utils.py`
- Add functional tests for `print_fires.py`