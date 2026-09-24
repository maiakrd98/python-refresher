test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_print_canada_fires python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Canada' \
    --country_column 0 \
    --fires_column 2
assert_in_stdout "[329, 683, 608, 627, 1546, 813, 1249, 3236, 1337, 222]"
assert_exit_code 0

run test_print_tanzania_crop_residues python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'United Republic of Tanzania' \
    --country_column 0 \
    --fires_column 3
assert_in_stdout "[615, 633, 670, 718, 687, 690, 732, 712, 701, 859]"
assert_exit_code 0

run test_print_canada_fires_mean python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Canada' \
    --country_column 0 \
    --fires_column 2 \
    --operation "mean"
assert_in_stdout "1065.0"
assert_exit_code 0

run test_print_tanzania_crop_residues_mean python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'United Republic of Tanzania' \
    --country_column 0 \
    --fires_column 3 \
    --operation "mean"
assert_in_stdout "701.7"
assert_exit_code 0

run test_canada_fires_median python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Canada' \
    --country_column 0 \
    --fires_column 2 \
    --operation "median"
assert_in_stdout "748.0"
assert_exit_code 0

run test_tanzania_crop_residues_median python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'United Republic of Tanzania' \
    --country_column 0 \
    --fires_column 3 \
    --operation "median"
assert_in_stdout "695.5"
assert_exit_code 0

run test_canada_fires_sd python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Canada' \
    --country_column 0 \
    --fires_column 2 \
    --operation "sd"
assert_in_stdout "876.540"
assert_exit_code 0

run test_tanzania_crop_residues_sd python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'United Republic of Tanzania' \
    --country_column 0 \
    --fires_column 3 \
    --operation "sd"
assert_in_stdout "66.356"
assert_exit_code 0

run test_file_not_found_error python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emisions_test_file.csv' \
    --country 'Spain' \
    --country_column 0 \
    --fires_column 3 \
    --operation "sd"
assert_in_stdout "Could not find test/func/Agrofood_co2_emisions_test_file.csv"
assert_exit_code 1

run test_result_column_index_error python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Spain' \
    --country_column 0 \
    --fires_column 23 \
    --operation "mean"
assert_in_stdout "result_column index (23) is out of bounds"
assert_exit_code 1

run test_query_column_index_error python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Spain' \
    --country_column 44 \
    --fires_column 2 \
    --operation "median"
assert_in_stdout "query_column index (44) is out of bounds"
assert_exit_code 1

run test_invalid_operation_error python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Spain' \
    --country_column 0 \
    --fires_column 2 \
    --operation "hi"
assert_in_stdout "Error: the argument 'operation' must be either 'mean', 'median', or 'sd'. It looks like you entered sonething else."
assert_exit_code 1

run test_empty_array_error python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Mars' \
    --country_column 0 \
    --fires_column 2 \
    --operation "mean"
assert_in_stdout "Error: there are no values in your query column (0) that match your query value ('Mars')."
assert_exit_code 1

run test_not_an_number_error python print_fires.py \
    --file_name 'test/func/Agrofood_co2_emissions_test_file.csv' \
    --country 'Canada' \
    --country_column 0 \
    --fires_column 0 \
    --operation "sd"
assert_in_stdout "Could not convert entry in result_column ('Canada') to float"
assert_exit_code 1
