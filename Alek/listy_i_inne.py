macierz = [[0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 1, 1]]

# for row in macierz:
#     for element in row:
#         print(element)
#
# for i in range(len(macierz)):
#     row = macierz[i]
#     for j in range(len(row)):
#         element = row[j]
#         print(element)

print("---------------------------------------")

def szukaj_rekurencyjnie(row, col):
    if col > 0:
        element = macierz[row][col-1]
        pozycja = (row, col-1)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            wszystkie_mokre_miejsca.add(pozycja)
            szukaj_rekurencyjnie(pozycja[0], pozycja[1])

    if row < len(macierz) - 1:
        element = macierz[row + 1][col]
        pozycja = (row + 1, col)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            wszystkie_mokre_miejsca.add(pozycja)
            szukaj_rekurencyjnie(pozycja[0], pozycja[1])

    if col < len(macierz[0]) - 1:
        element = macierz[row][col + 1]
        pozycja = (row, col + 1)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            wszystkie_mokre_miejsca.add(pozycja)
            szukaj_rekurencyjnie(pozycja[0], pozycja[1])

    if row > 0:
        element = macierz[row - 1][col]
        pozycja = (row - 1, col)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            wszystkie_mokre_miejsca.add(pozycja)
            szukaj_rekurencyjnie(pozycja[0], pozycja[1])

    return ...

dlugosc = len(macierz[0])
wszystkie_mokre_miejsca = set()  # pojedyncze punkty
wszystkie_rzeki = set()  # cale rzeki

for i in range(dlugosc):
    for j in range(len(macierz)):
        element = macierz[j][i]
        pozycja = (j, i)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            aktualna_rzeka = set()
            wszystkie_mokre_miejsca.add(pozycja)
            szukaj_rekurencyjnie(j, i)
            wszystkie_rzeki.add(tuple(aktualna_rzeka))

print(wszystkie_rzeki)
print(wszystkie_mokre_miejsca)


x = [1,2,3]

def a(b):
    b.append(1)
    print(x)

print(x)
a(x)
print(x)