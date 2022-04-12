farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("---")
print("Indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)

# print("Indexing a set is not possible")
# goat = farm_animals[3]

more_animals = {'sheep', 'cow', 'hen', 'goat', 'horse'}
if more_animals == farm_animals:
    print('The sets are equal')
else:
    print('The sets are different')
