import my_utils

country = 'Canada'
country_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires = my_utils.get_column(file_name, country_column, country, fires_column)
print(fires)
