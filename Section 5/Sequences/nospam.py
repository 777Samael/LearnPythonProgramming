menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#
#     else:
#         top_index = len(meal) - 1
#         for index, item in enumerate(reversed(meal)):
#             if item == "spam":
#                 del meal[top_index - index]
#         print(meal)

# for meal in menu:
#
#     new_meal = []
#     for item in meal:
#         if item != "spam":
#             new_meal.append(item)
#     print(new_meal)
