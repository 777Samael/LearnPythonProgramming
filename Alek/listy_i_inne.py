macierz = [[0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 1, 1]]

for row in macierz:
    for element in row:
        print(element)

for i in range(len(macierz)):
    row = macierz[i]
    for j in range(len(row)):
        element = row[j]
        print(element)

print("---------------------------------------")

dlugosc = len(macierz[0])
wszystkie_mokre_miejsca = set()  # pojedyncze punkty
wszystkie_rzeki = set()  # cale rzeki
for i in range(dlugosc):
    for j in range(len(macierz)):
        element = macierz[j][i]
        pozycja = (j,i)
        if element == 1 and pozycja not in wszystkie_mokre_miejsca:
            wszystkie_mokre_miejsca.add(pozycja)


            # aktualna_rzeka = {}

            # dodaj te 1 do aktualnej rzeki
            # sprawdz sąsiada, ale tylko takiego, ktrego nie mamy w mokrych_miejscach

# macierz[nr_wiersza][nr_kolumny]

# Kolumnowo
macierz[0][
    0]  # j=max 4 czyli dlugosz listy macierzy czyli ilosc wierszy      i=ilosc kolumn czyli, czli 4 czyli len(macierz[0])
macierz[1][0]
macierz[2][0]
macierz[3][0]
macierz[4][0]
macierz[0][1]

# Wierszowo
macierz[0][0]
...
macierz[0][5]
macierz[1][0]
