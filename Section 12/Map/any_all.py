entries = [1, 2, 3, 4, 5]

print(f"all: {all(entries)}")
print(f"any: {any(entries)}")

print("iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]

print(f"all: {all(entries_with_zero)}")
print(f"any: {any(entries_with_zero)}")

print()
print("Values interpreted as False in Python")
print(f"""False: {False}
None: {bool(None)}
0: {bool(0)}
0.0: {bool(0.0)}
empty list []: {bool([])}
empty tuple (): {bool(())}
empty string '': {bool('')}
empty string "": {bool("")}
empty mapping {{}}: {bool({})}
""")

print("=" * 80)
name = "Tim"
if name:
    print("Hello {}".format(name))
else:
    print("Welcome, person with no name")