text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]

print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')
print(lc_words)
