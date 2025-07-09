
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#import numpy as np
import wykresyGantta
#M1 = [5,4,2,6,1,3,4,1,6,2]
#M2 = [1,2,4,1,0,3,1,1,5,1]

M1 = [7,2,5,3,1,6,3,4]
M2 = [4,0,2,1,3,5,3,3]


mniejszeM1 = []
mniejszeM2 = []

indeksyM1 = []
indeksyM2 = []


for i in range(len(M1)):
    if M1[i] <= M2[i]:
        mniejszeM1.append(M1[i])
        indeksyM1.append(i)
    else:
        mniejszeM2.append(M2[i])
        indeksyM2.append(i)

posortowaneM1 = sorted(zip(mniejszeM1,indeksyM1),key=lambda x: (x[0], -x[1]))
posortowaneM2 = sorted(zip(mniejszeM2,indeksyM2),key=lambda x: (x[0], -x[1]),reverse=True)

_, indeksyPosortowane1 = zip(*posortowaneM1)
_, indeksyPosortowane2 = zip(*posortowaneM2)

#print(indeksyPosortowane1)

#`print(indeksyPosortowane2)


M = [M1 , M2]

posortowaneIndeksy = indeksyPosortowane1 + indeksyPosortowane2
liczbaMaszyn = wykresyGantta.gantt(M,posortowaneIndeksy)







