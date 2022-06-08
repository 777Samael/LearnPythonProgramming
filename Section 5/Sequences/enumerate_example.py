for index, character in enumerate("abcdefgh"):
    print(index, character)

print("---")

for index, character in enumerate("abcdefgh", start=1):
    print(index, character)

print("---")

for t in enumerate("abcdefgh"):
    print(t)

print("---")

index, character = (0, 'a')
print(index)
print(character)

print("---")

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)
