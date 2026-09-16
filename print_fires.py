import my_utils
import argparse


def main():
    parser = argparse.ArgumentParser(
                        prog='print_fires',
                        description='Prints given column from given country')

    parser.add_argument('--country',
                        type=str,
                        help='Country you are interested in',
                        required=True)

    parser.add_argument('--country_column',
                        type=int,
                        help='Column in which countries are listed',
                        required=True)

    parser.add_argument('--fires_column',
                        type=int,
                        help='Column in which wildfire emmissions are listed',
                        required=True)

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file',
                        required=True)

    args = parser.parse_args()

    fires = my_utils.get_column(args.file_name, args.country_column,
                                args.country, result_column=args.fires_column)
    print(fires)


if __name__ == "__main__":
    main()
