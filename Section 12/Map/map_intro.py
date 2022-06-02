import timeit

text = "what have the romans ever done for us"


def comp_caps():
    capitals = [char.upper() for char in text]
    print(capitals)


# use map
def map_caps():
    map_capitals = list(map(str.upper, text))
    print(map_capitals)


def comp_wrds():
    words = [word.upper() for word in text.split(' ')]
    print(words)


# use map
def map_wrds():
    map_words = list(map(str.upper, text.split(' ')))
    print(map_words)


# for x in map(str.upper, text.split(' ')):
#     print(x)

# result1 = timeit.repeat(comp_caps, number=10000)
# result2 = timeit.repeat(map_caps, number=10000)
# result3 = timeit.repeat(comp_wrds, number=10000)
# result4 = timeit.repeat(map_wrds, number=10000)
# print(result1)
# print(result2)
# print(result3)
# print(result4)

if __name__ == '__main__':
    # print(comp_caps())
    # print(map_caps())
    # print(comp_wrds())
    # print(map_wrds())
    # print(timeit.timeit("comp_caps()", setup="from map_intro import comp_caps", number=10000))
    print(timeit.timeit(comp_caps, number=1000))
    print(timeit.timeit(map_caps, number=1000))
    print(timeit.timeit(comp_wrds, number=1000))
    print(timeit.timeit(map_wrds, number=1000))
