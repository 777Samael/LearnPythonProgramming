from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

tim = Player("Tim")

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

ugly_troll = Troll("Pug")
print(f"Ugly troll - {ugly_troll}")

another_troll = Troll("Ug")
print(f"Another troll - {another_troll}")

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

brother.take_damage(10)
print(brother)

print("---")

big_vamp = Vampyre("Nosferatu")
print(big_vamp)

# while big_vamp._alive:
#     big_vamp.take_damage(2)
#     print(big_vamp)

king_vamp = VampyreKing("Dodo")
print(king_vamp)

while king_vamp._alive:
    king_vamp.take_damage(16)
    print(king_vamp)
