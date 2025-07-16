import math
import numpy as np

def posortowanie(M1,M2):
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

    if mniejszeM1 != []:
        posortowaneM1 = sorted(zip(mniejszeM1,indeksyM1),key=lambda x: (x[0], x[1]))
        _, indeksyPosortowane1 = zip(*posortowaneM1)
    
    
    if mniejszeM2 != []:
        posortowaneM2 = sorted(zip(mniejszeM2,indeksyM2),key=lambda x: (x[0], -x[1]),reverse=True)
        _, indeksyPosortowane2 = zip(*posortowaneM2)
    
    if mniejszeM1 != [] and mniejszeM2 != []:
        kolejnosci = indeksyPosortowane1 + indeksyPosortowane2
    elif mniejszeM1 == [] and mniejszeM2 !=[]:
        kolejnosci = indeksyPosortowane2
    elif mniejszeM1 != [] and mniejszeM2 ==[]:
        kolejnosci = indeksyPosortowane1
    else:
        return 0
        

    return kolejnosci

def Johnson(M,roznaKolejnosc):
    
    kolejnosci = []
    liczbaMaszyn = sum(1 for element in M if isinstance(element, list))


# Problem dwóch maszyn
    if liczbaMaszyn == 2:
        kolejnosci = posortowanie(M[0],M[1])
        return kolejnosci


# Uproszczenie do problemu dwóch maszyn
    elif (liczbaMaszyn > 2 and not roznaKolejnosc):
        k = math.ceil(liczbaMaszyn/2)
        M1 = np.sum(M[0:k], axis = 0)
        M2 = np.sum(M[k:],axis = 0) 
        kolejnosci = posortowanie(M1,M2)
        return kolejnosci 


# Różna kolejność na parach maszyn

# Parzysta liczba maszyn 
    elif liczbaMaszyn > 3 and roznaKolejnosc:
        k = math.floor(liczbaMaszyn/2)
        
        if liczbaMaszyn % 2 == 0:
            for j in range(k):
                kolejnosc = posortowanie(M[2*j],M[2*j+1])
                kolejnosci.append(kolejnosc)
               
# Nieparzysta liczba maszyn
        else:
            for j in range(k):
                if j != k-1:
                    kolejnosc = posortowanie(M[2*j],M[2*j+1])
                    kolejnosci.append(kolejnosc)
                else:
                    M1 = np.sum(M[-3:-1], axis = 0)
                    M2 = M[-1]
                    kolejnosc = posortowanie(M1,M2)
                    kolejnosci.append(kolejnosc)


        return kolejnosci