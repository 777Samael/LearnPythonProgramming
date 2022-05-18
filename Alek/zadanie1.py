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
from statistics import median
from numpy import interp

input_data = [600, 632, 680, 690, 600, 632, 680, 690, 600, 632, 680, 690, 0, 0, 700, 690, 600, 632, 680, 690, 1054, 700,
              690, 720, 720, 750, 760, 770, 740]
input_range = [0, 1054]
output_range = [-20, 100]
avg_list = []

# Mediany

# def median
# def sortujaca


def sortujaca(array):

    array_length = len(array)
    for x in range(array_length):
        for y in range(0, array_length - x - 1):
            if array[y] > array[y + 1]:
                temp = array[y]
                array[y] = array[y + 1]
                array[y + 1] = temp
    return array


def mediana(data):
    """
    Return median value for provided data

    :param data: list of values
    :return:
    """
    sorted_args = sortujaca(data)
    if len(sorted_args) % 2 == 0:
        n1 = sorted_args[len(sorted_args) // 2 - 1]
        n2 = sorted_args[len(sorted_args) // 2]
        result = (n1 + n2) / 2
    else:
        result = sorted_args[len(sorted_args) // 2]
    return result


for index, value in enumerate(input_data):
    sample_list = input_data[max(0, index - 4):index + 1]  # pierwszy krok jest spoko
    median_value = mediana(sample_list)
    mapped_value = interp(median_value, input_range, output_range)  # TO jest spoko ale mean bym zamienii na median i rozbi to
    # znalexc jak sobie rondowac cos do 2 miejsca z intem i przy princie
    print(f'Mediana z ostatnich {len(sample_list)} sek.: {mapped_value:.2f}')
    sleep(1)
