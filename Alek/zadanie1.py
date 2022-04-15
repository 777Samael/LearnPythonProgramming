# DHT22


# 0 - 1054 <--- opornosc
# -20 - 100 <--- temperatura


# co sekundę otrzymuejmy odczyt z czujnika i chcemy przedstawić userowi temeraturę


# [600 632 680 690 600 632 680 690 600 632 680 690 0 0 700 690 600 632 680 690 1054 700 690 720 720 750 760 770 740 ] # 1hz


# 1. czegos co generuje nam dane
#      a) Jesli uruchomimy program to będzie dzialal do momentu az go zatrzymamy (while True)
#      b) podaje ten zestaw [600 632 680 690 600 632 680 690 600 632 680 690 0 0 700 690 600 632 680 690 1054 700 690 720 720 750 760 770 740 ]
#       (poczatkowo po tych 20 elementach moze sie program konczyc)
#     c)  wyprintuj przeskalowaną opronosc (z 600 na temperature)

from time import sleep
from statistics import mean
from numpy import interp

input_data = [600, 632, 680, 690, 600, 632, 680, 690, 600, 632, 680, 690, 0, 0, 700, 690, 600, 632, 680, 690, 1054, 700,
              690, 720, 720, 750, 760, 770, 740]
avg_list = []

#Mediany

# def median
# def sortujaca


for index, value in enumerate(input_data):
    avg_list = input_data[max(0, index - 4):index + 1]  # pierwszy krok jest spoko
    output_value = round(
        interp((mean(avg_list)), [0, 1054], [-20, 100]))  # TO jest spoko ale mean bym zamienii na median i rozbi to
    # znalexc jak sobie rondowac cos do 2 miejsca z intem i przy princie
    print(f'średnia z ostatnich {len(avg_list)} sek.: {output_value}')
    sleep(1)
