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


def szukaj_rekurencyjnie(row, col, rzeka):

    wszystkie_mokre_miejsca.add((row, col))
    rzeka.add((row, col))
    if col > 0:
        element = macierz[row][col-1]
        pozycja = (row, col-1)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            szukaj_rekurencyjnie(pozycja[0], pozycja[1], rzeka)

    if row < len(macierz) - 1:
        element = macierz[row + 1][col]
        pozycja = (row + 1, col)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            szukaj_rekurencyjnie(pozycja[0], pozycja[1], rzeka)

    if col < len(macierz[0]) - 1:
        element = macierz[row][col + 1]
        pozycja = (row, col + 1)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            szukaj_rekurencyjnie(pozycja[0], pozycja[1], rzeka)

    if row > 0:
        element = macierz[row - 1][col]
        pozycja = (row - 1, col)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            szukaj_rekurencyjnie(pozycja[0], pozycja[1], rzeka)



dlugosc = len(macierz[0])
wszystkie_mokre_miejsca = set()  # pojedyncze punkty
wszystkie_rzeki = set()  # cale rzeki

for i in range(dlugosc):
    for j in range(len(macierz)):
        element = macierz[j][i]
        pozycja = (j, i)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            aktualna_rzeka = set()
            szukaj_rekurencyjnie(j, i, aktualna_rzeka)
            wszystkie_rzeki.add(tuple(aktualna_rzeka))

# print(wszystkie_rzeki)
for x in wszystkie_rzeki:
    print(f"{x} dlugosc: {len(x)}")
print("---------------------------------------")
print(len(max(wszystkie_rzeki)))

# doniczka > kompozycja z klas roślina i czujnik