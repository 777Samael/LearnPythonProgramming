def factorial(number: int) -> int:
    """
    Calculate factorial of given int.

    :param number: Value to be calculated
    :return: Factorial value of given number
    """
    fact = 1

    if number == 0:
        return fact

    for i in range(1, number + 1):
        fact = fact * i
    return fact


for i in range(36):
    print("{} {}".format(i, factorial(i)))
