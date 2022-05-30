def avarage(*args):
    print(type(args))
    print(f"args is : {args}")
    print("*args is : ", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def build_tuple(*args):
    return args


print(avarage(1, 2, 3, 4))

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)
