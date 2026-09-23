import sys
import statistics


def get_column(file_name, query_column, query_value, result_column=1):
    """ Opens a file and returns the values in the results column for which \
    the value of the query column matches the query value

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
        List of the values in results_column for which the value of \
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

    file.close()

    return results


def mean(array):
    """ Returns the arithmetic mean of a non-empty array of integers.

    Parameters
        ----------
        array : list of int
            The array that you would like to find the mean of. Must be \
            non-empty.

    Returns
        -------
        mean : float
            The arithmetic mean of the values in array.
    """

    if len(array) == 0:
        print("It looks like you input an empty array. The function mean() "
              "only takes non-empty arrays.")
        sys.exit(1)

    if (not all(type(i) is int for i in array)):
        print("At least one of the entries in the array you input is not an "
              "integer. The function mean() only takes arrays of integers.")
        sys.exit(1)

    mean = sum(array)/len(array)

    return mean


def median(array):
    """ Returns the median of a non-empty array of integers.

    Parameters
        ----------
        array : list of int
            The array that you would like to find the median of. Must be \
            non-empty.

    Returns
        -------
        median : float
            The median of the values in array. If there are an even number of \
            entries in array, this is the arithmetic mean of the two middle \
            values.
    """

    if len(array) == 0:
        print("It looks like you input an empty array. The function median() "
              "only takes non-empty arrays.")
        sys.exit(1)

    if (not all(type(i) is int for i in array)):
        print("At least one of the entries in the array you input is not an "
              "integer. The function median() only takes arrays of integers.")
        sys.exit(1)

    sorted_array = sorted(array)

    mid_index = len(sorted_array) // 2

    # odd number of elements
    if len(sorted_array) % 2 != 0:
        median = float(sorted_array[mid_index])

    # even number of elements
    else:
        median = (sorted_array[mid_index-1]+sorted_array[mid_index])/2

    return median


def sd(array):
    """ Returns the standard deviation of a non-empty array of integers.

    Parameters
        ----------
        array : list of int
            The array that you would like to find the standard deviation of. \
            Must be non-empty.

    Returns
        -------
        sd : float
            The sample standard deviation of the values in array.
    """

    if len(array) == 0:
        print("It looks like you input an empty array. The function sd() "
              "only takes non-empty arrays.")
        sys.exit(1)

    if (not all(type(i) is int for i in array)):
        print("At least one of the entries in the array you input is not an "
              "integer. The function sd() only takes arrays of integers.")
        sys.exit(1)

    sd = statistics.stdev(array)

    return sd
