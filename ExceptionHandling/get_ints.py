import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number, entered, please try again")
        except EOFError:
            sys.exit(0)
        finally:
            print("The finally clause always executes")


first_number = getint("Please enter first number: ")
second_number = getint("Please enter second number: ")

try:
    print(f"{first_number} divided by {second_number} is {first_number / second_number}")
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")
