import sys


def get_column(file_name, query_column, query_value, result_column=1):
    results = []

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)

    for line in file:

        entries = line.split(sep=',')

        try:
            query_entry = entries[query_column]
        except IndexError:
            print('query_column index is out of bounds')
            sys.exit(1)

        if query_entry == query_value:

            try:
                result_entry = entries[result_column]
            except IndexError:
                print('result_column index is out of bounds')
                sys.exit(1)

            try:
                result_float = float(result_entry)
            except ValueError:
                print("Could not convert entry in result_column ('" +
                      result_entry + "') to float")
                sys.exit()

            results.append(round(result_float))

    return results
