vehicles = {
    'dream': 'Honda 250T',
    # 'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
    }

# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5")
# print(learner)
#
# learner = vehicles.get("ER5")
# print(learner)
#
# my_car = vehicles['Fiesta']
# print(my_car)

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

vehicles["starfighter"] = "lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
# result = vehicles.pop("f1", None)
result = vehicles.pop("f1", "You wish!")
print(result)
print("---")

plane = vehicles.pop("learjet")
print(plane)
print("---")

bike = vehicles.pop("tenere", "not present")
print(bike)

print("---")
for key, value in vehicles.items():
    print(key, value, sep=", ")
