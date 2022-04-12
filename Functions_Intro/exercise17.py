def fizz_buzz(number: int) -> str:
    """
    Return the correct word ("fizz", "buzz" or "fizz buzz"), or the number if it's not divisible by either 3 or 5.

    :param number: Value to test for divisibility by 3 or 5
    :return: Returned value
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz.  Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well, done you reached {}".format(next_number))

# LOW = 1
# HIGH = 100
#
# for i in range(LOW, HIGH + 1):
#     tested_value = fizz_buzz(i)
#     print("For {} you can say: {}".format(i, tested_value))
