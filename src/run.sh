#!/bin/bash
echo

echo "Example 1: Successful run"
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'Canada' --country_column 0  --fires_column 3
echo

echo "Example 2: Error due to typo in file"
python print_fires.py --file_name 'Agrofood_co2_emision.csv' --country 'Canada' --country_column 0  --fires_column 3
echo

echo "Example 3: Error due to too large column index"
python print_fires.py --file_name 'Agrofood_co2_emission.csv' --country 'Canada' --country_column 0  --fires_column 31
echo
