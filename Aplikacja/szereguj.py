import wykresyGantta
import algorytmJohnsona


def przekarz(M,roznaKolejnosc):

    M = [
    [int(x) if x else 0 for x in inner_list]  # konwersja pojedynczego wiersza
    for inner_list in M      # iteracja po wierszach (listach)
]
    print(M)
    #roznaKolejnosc = False # Powinno być określane w aplikacji 
    posortowaneIndeksy = algorytmJohnsona.Johnson(M,roznaKolejnosc)

    #print(posortowaneIndeksy)

    if roznaKolejnosc:
        Cmax, Fsrd = wykresyGantta.gantt2(M,posortowaneIndeksy)
    else:
        Cmax, Fsrd = wykresyGantta.gantt(M,posortowaneIndeksy)
