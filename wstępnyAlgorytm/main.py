
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import numpy as np
import wykresyGantta
import algorytmJohnsona

#M1 = [5,4,2,6,1,3,4,1,6,2]
#M2 = [1,2,4,1,0,3,1,1,5,1]

#M1 = [7,2,5,3,1,6,3,4]
#M2 = [4,0,2,1,3,5,3,3]
#M = [M1 , M2]

#M = [[2,5,8,6],[4,2,2,9],[0,2,1,5],[3,7,9,8],[3,0,2,1]]

#M = [[3,2,1,5,4,3,2],[1,3,4,5,2,2,1],[1,2,2,5,1,3,6],[2,3,5,5,2,4,3]] # Powinno być wprowadzane z aplikacji 

#M = [[2,4,1,6,3,1],[2,3,2,5,5,3]]

M = [[1,2,3,4,3,2,1],[2,3,2,1,4,2,3],[3,4,1,2,1,3,2],[2,1,4,2,3,1,4],[1,2,2,3,2,3,1],[2,1,3,2,1,2,3],[1,3,2,2,2,1,2]]

#M = [[1,2,3,4,3,2,1],[2,3,2,1,4,2,3],[3,4,1,2,1,3,2],[2,1,4,2,3,1,4],[1,2,2,3,2,3,1],[2,1,3,2,1,2,3]]

print(M)
roznaKolejnosc = True # Powinno być określane w aplikacji 

posortowaneIndeksy = algorytmJohnsona.Johnson(M,roznaKolejnosc)

print(posortowaneIndeksy)

if roznaKolejnosc:
    Cmax, Fsrd = wykresyGantta.gantt2(M,posortowaneIndeksy)
else:
    Cmax, Fsrd = wykresyGantta.gantt(M,posortowaneIndeksy)

print(Cmax)
print(Fsrd)











