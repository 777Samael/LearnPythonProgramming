# def print_backwards(*args, file=None):
#     for word in args[::-1]:
#         print(word[::-1], end=' ', file=file)
# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)   # print first word separately
    # print(end=end_character)


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another String")

print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print('='*10)
