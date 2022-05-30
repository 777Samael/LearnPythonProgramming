def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


# odds = oddnumbers()

# for i in range(100):
#     print(next(odds))

def pi_series():
    odds = oddnumbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(1000000):
    print(next(approx_pi))
