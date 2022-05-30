import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: remove after testing

# print("Please guess number between 1 and {}: ".format(highest))
# guess = int(input())
#
# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater that answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")

# print("Please guess number between 1 and {}: ".format(highest))
# guess = int(input())
# while guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#         guess = int(input())
#     else:
#         print("Please guess lower")
#         guess = int(input())
#
# print("Well done, you guessed it")

guess = 0
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater that answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")
