import my_utils
import argparse

parser = argparse.ArgumentParser(
                    prog='print_fires',
                    description='Prints a given column from a given country')

parser.add_argument('--country',
                    type=str,
                    help='The country you are interested in',
                    required=True)

parser.add_argument('--country_column',
                    type=int,
                    help='The column in which countries are listed',
                    required=True)

parser.add_argument('--fires_column',
                    type=int,
                    help='The column in which wildfire emmissions are listed',
                    required=True)

parser.add_argument('--file_name',
                    type=str,
                    help='The name of the file',
                    required=True)

args = parser.parse_args()

fires = my_utils.get_column(args.file_name, args.country_column, args.country,
                            result_column=args.fires_column)
print(fires)
