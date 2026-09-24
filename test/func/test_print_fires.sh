test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# is it ok to run these from the func directory?

run test_print_canada_fires python ../../print_fires.py --file_name 'Agrofood_co2_emissions_test_file.csv' --country 'Canada' --country_column 0  --fires_column 2 
assert_in_stout "[329, 683, 608, 627, 1546, 813, 1249, 3236, 1337, 222]"
assert_exit_code 0

run test_print_tanzania_crop_residues python ../../print_fires.py --file_name 'Agrofood_co2_emissions_test_file.csv' --country 'United Republic of Tanzania' --country_column 0  --fires_column 3 
assert_in_stout "[615, 633, 670, 718, 687, 690, 732, 712, 701, 859]"
assert_exit_code 0

# TD DO: negative tests????
#run test_print_canada_no_spain python print_fires.py --file_name 'Agrofood_co2_emissions_test_file.csv' --country 'Canada' --country_column 0  --fires_column 3 
#assert_in_stout ""
#assert_exit_code 0

# TO DO: also one for no crop residues in forest fires???

run test_print_canada_fires_mean python ../../print_fires.py --file_name 'Agrofood_co2_emissions_test_file.csv' --country 'Canada' --country_column 0  --fires_column 2 --operation "mean"
assert_in_stout "1065.0"
assert_exit_code 0

run test_print_tanzania_crop_residues_mean python ../../print_fires.py --file_name 'Agrofood_co2_emissions_test_file.csv' --country 'United Republic of Tanzania' --country_column 0  --fires_column 3 --operation "mean"
assert_in_stout "701.7"
assert_exit_code 0

# TO DO: error testing 