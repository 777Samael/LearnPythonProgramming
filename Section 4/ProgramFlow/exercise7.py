quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

capitals = ""

for character in quote:
    if not character.islower() and character.isalpha():
        capitals = capitals + character

print(capitals)
