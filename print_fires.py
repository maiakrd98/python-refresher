import my_utils
import argparse
import sys


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

    parser.add_argument('--operation',
                        type=str,
                        help='Operation to perform on the returned values',
                        required=False)

    args = parser.parse_args()

    fires = my_utils.get_column(args.file_name, args.country_column,
                                args.country, result_column=args.fires_column)

    if args.operation is None:
        print(fires)

    elif args.operation == "mean":
        print(my_utils.mean(fires))

    elif args.operation == "median":
        print(my_utils.median(fires))

    elif args.operation == "sd":
        print(my_utils.sd(fires))

    else:
        print("Error: the argument 'operation' must be either 'mean', "
              "'median', or 'sd'. It looks like you entered sonething else.")
        sys.exit(1)


if __name__ == "__main__":
    main()
