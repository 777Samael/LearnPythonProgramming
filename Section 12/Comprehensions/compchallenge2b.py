locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

print("nested for loops")
print("---")

for loc in sorted(locations):
    exits_to_destination_1 = []
    for ext in exits:
        if loc in exits[ext].values():
            exits_to_destination_1.append((ext, locations[ext]))
    print(f"Location leading to {loc}", end='\t')
    print(exits_to_destination_1)

print("---")

print("List comprehension inside a for loop")
print("---")

for loc in sorted(locations):
    exits_to_destination_2 = [(ext, locations[ext]) for ext in exits if loc in exits[ext].values()]
    print(f"Location leading to {loc}", end='\t')
    print(exits_to_destination_2)

print("---")

print("Nested comprehension")

print("---")

exits_to_destination_3 = [[(ext, locations[ext]) for ext in exits if loc in exits[ext].values()]
                          for loc in sorted(locations)]
print(exits_to_destination_3)

print("---")

for index, loc in enumerate(exits_to_destination_3):
    print(f"Location leading to {index}", end='\t')
    print(loc)
