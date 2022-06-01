burgers = ["beef", "chicken", "spicy bean"]
toppings = {"cheese", "egg", "beans", "spam"}

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

print("---")

for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print("---")

for burger in burgers:
    for topping in toppings:
        print((burger, topping))

print("---")

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

print("---")

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meals)
