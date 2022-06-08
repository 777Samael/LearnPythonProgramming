# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.
 
 
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

# the_forest = [(key, locations[key]) for key, value in exits.items() if 5 in value.values()]
# print(the_forest)

for key_loc, value_loc in locations.items():
    the_forest = [(key, locations[key]) for key, value in exits.items() if key_loc in value.values()]
    print(f"Location number {key_loc}\n\t{the_forest}")

# for key, value in exits.items():
#     if 5 in value.values():
#         print(f"Key: {key}, Desc: {locations[key]}")
#
#     print(value.values())
#     print(f"Key: {key}\t|\tValue: {value}")
#     for key2, value2 in value.items():
#         print(f"\tKey2: {key2}\t|\tValue2: {value2}")


# the_forest = [value for key, value in exits.items() if key == 5]
# print(the_forest)

# meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
# print(meals)
# for key, value in available_parts.items():
