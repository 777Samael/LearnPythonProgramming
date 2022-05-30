# x = 8 - 5
# y = x / 0

def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculate n! recursively"""
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * n * factorial(n-1)


try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program can't calculate factorials that large")
except ZeroDivisionError:
    print("What are you doing dividing by zero???")

print("Program terminating")
