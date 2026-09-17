# Python Refresher
This repository contains code for reading a file containing data on greenhouse gas emissions from various sources and various countries and printing the emissions from a particular country and a particular source.

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
conda activate swe4s
```

This environment contains `pycodestyle` for checking that python code is compliant with the PEP 8 style guide.

## Data file
This repository expects a file called `Agrofood_co2_emission.csv`. This should be a comma separated file with countries listed in the first column, years listed in the second column, and corresponding greenhouse gas emmissions from various sources listed in the remaining columns.

## Usage examples

`print_fires.py` takes in four command line inputs: `--file_name`, which is the name of the data file, `--country`, which is the country you are interested in, `--country_column`, which is the column that the countries are listed in, and `--fires_column`, which is the column where the fire emmissions (or other emmissions of interest) are listed. It then uses the function `get_column()` in `my_utils.py` to open the file and return the values in the fires column for which the value of the country column matches the given country. It also converts those values to integers.

For example, running
```
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'Canada' --country_column 0  --fires_column 3
```
will print a vector of emmissions due to fires in Canada for each year between 1990 and 2020, since fire emmissions are listed in the fourth column of `Agrofood_co2_emission.csv`. Similarly, running 
```
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'Afghanistan' --country_column 0  --fires_column 17
```
will print a vector of emmissions due to fertilizer manufacturing in Afghanistan for each year between 1990 and 2020, since fertilizer manufacturing emmissions are listed in the eighteenth column of `Agrofood_co2_emission.csv`.

You can also run several examples using `run.sh` as follows:
```
./run.sh
```
This will perform one successful run, one run that gives an error due to a typo in the file name, and one run that gives an error because one of the column numbers is too large/out of bounds.

To check that the files follow the PEP 8 style guide, run
```
pycodestyle print_fires.py my_utils.py
```
