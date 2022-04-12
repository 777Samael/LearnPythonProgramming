import copy

animals = {
    "loin": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

things = copy.deepcopy(animals)

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print("---")

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
