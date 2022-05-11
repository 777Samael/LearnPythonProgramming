from player import Player

tim = Player("Tim")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim._lives = 9
print(tim)

tim.level = 2
print(tim)

tim.level += 5
print(tim)

tim.level = 3
print(tim)

tim.score = 500
print(tim)
