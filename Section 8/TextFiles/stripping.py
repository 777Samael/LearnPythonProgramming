def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]  # Return a copy of `string`.


def removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):  # suffix='' should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]


filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

chars = "'Twas"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

chars = "'Twasebv"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

chars = "' Twasebv"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

print("---")

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix('toves')
print(toves_removed)

print("---")

twas_removed = removeprefix(first, "'Twas")
print(twas_removed)
toves_removed = removesuffix(first, 'toves')
print(toves_removed)
