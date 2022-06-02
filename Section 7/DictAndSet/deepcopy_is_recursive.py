from simple_deepcopy import my_deepcopy
import copy

original = {
    "Tim": ["Buczanka", ["Programmer", "Teacher"]],
    "JP2": ["Robert", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["JP2"].append("UK")

original["Tim"][1].append("Cashier")
jp_list = original["JP2"]
jp_list[1].append("Courier")

print("Original: ", original)
print("Copy_1: ", copy_1)
print("Copy_2: ", copy_2)
