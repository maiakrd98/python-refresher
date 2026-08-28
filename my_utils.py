def get_column(file_name, query_column, query_value, result_column):
    results = []

    with open(file_name) as file:
        for line in file:

            entries = line.split(sep=',')

            if entries[query_column] == query_value:
                results.append(entries[result_column])

    return results
