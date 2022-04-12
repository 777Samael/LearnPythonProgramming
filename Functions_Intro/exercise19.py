def sum_numbers(*args: float) -> float:
    """
    Calculate the sum of all numbers passed as arguments.

    :param args: Provided numbers
    :return: sum of provided numbers
    """
    return sum(args)


print(sum_numbers(1.1, 2.2, 5.5))
