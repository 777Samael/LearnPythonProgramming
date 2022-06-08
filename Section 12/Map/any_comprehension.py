from data import people, plants_list, plants_dict

# people = []

if bool(people) and ([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

print("---")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

print("---")
# comprehension solution
if any([plant.plant_type == "Grass" for key, plant in plants_dict.items()]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

print("---")
# generator solution
if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

print("---")
# generator iterating over keys
if any(plants_dict[key].plant_type == "Grass" for key in plants_dict):
    print("This pack contains grass")
else:
    print("No grasses in this pack")
