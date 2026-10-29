def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    values_sorted = sorted(values)
    return values_sorted[-1:-4:-1]
    pass