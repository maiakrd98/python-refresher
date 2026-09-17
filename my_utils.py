import sys


def get_column(file_name, query_column, query_value, result_column=1):
    """ Opens a file and returns the values in the results column for which the
    value of the query column matches the query value

    Parameters
    ----------
    file_name : str
        Name of file to be opened

    query_column : int
        Column to match to query_value

    query_value
        Desired value of query_column

    results_column : int, optional (default = 1)
        Column with values to be returned

    Returns
    -------
    results : list of int
        List of the values in results_column for which the value of
        query_column matches query_value
    """

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
            print('query_column index (' + str(query_column) +
                  ') is out of bounds')
            sys.exit(1)

        if query_entry == query_value:

            try:
                result_entry = entries[result_column]
            except IndexError:
                print('result_column index (' + str(result_column) +
                      ') is out of bounds')
                sys.exit(1)

            try:
                result_float = float(result_entry)
            except ValueError:
                print("Could not convert entry in result_column ('" +
                      result_entry + "') to float")
                sys.exit()

            # round results to the nearest integer
            # (nearest even integer if the number ends in .5)
            results.append(round(result_float))

    return results
