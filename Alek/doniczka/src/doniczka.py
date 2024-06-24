from czujnik import Czujnik
from roslina import Roslina


class Doniczka:

    def __init__(self, a: Roslina, b: Czujnik):
        self.a = a
        self.b = b

    def podlej(self):
        ...

    def czy_podlac(self) -> bool:
        return self.b.pomiar() > self.a.zapotrzebowanie


# rozrysować strukturę działania doniczki
# zależności między elementami i co się powinno dziać
# moze dodać typ rośliny żeby nadać ine ilości zapotrzebowania na wodę
# zapotrzebowanie -> {"nazwa_rosliny": ["ilosc_wody", "interwal_podlewania", "docelowa_wilgotnosc"]}
#              START
#                |
#       doniczka: wybierz rosline z listy
#       ---------------------------------
#       |                               |
#       | (jest na liście)              | (brak na liście)
#       |                               |
#   doniczka:                           doniczka:
#   pobierz parametry z bazy            pobierz parametry od usera
#       |                               |
#       ---------------------------------
#                       |
#                   czujnik:
#                    pomiar
#                       |
#                   doniczka:
#                   czy_podlac
#                       |
#               ---------------------
#              t|                  n|
#              doniczka:           doniczka:
#              czy jest woda       czekaj interwal
#               ---------------
#              t|            n|
#           doniczka:        doniczka:
#           podlej           powiadom usera
#               |
#           doniczka:
#           czekaj interwal
#
# dodać zapisywanie do bazy stanu aktualnego, żeby dało się wznowić pracę po przerwaniu





