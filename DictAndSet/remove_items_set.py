small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

print("---")

small_ints.discard(99)
# small_ints.remove(99)
print(small_ints)

