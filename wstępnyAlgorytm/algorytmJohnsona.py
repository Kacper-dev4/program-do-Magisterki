import math
import numpy as np
def Johnson(M,roznaKolejnosc):
    
    kolejnosci = []
    liczbaMaszyn = sum(1 for element in M if isinstance(element, list))


# Problem dwóch maszyn
    if liczbaMaszyn == 2:

        mniejszeM1 = []
        mniejszeM2 = []

        indeksyM1 = []
        indeksyM2 = []


        for i in range(len(M[0])):
            if M[0][i] <= M[1][i]:
                mniejszeM1.append(M[0][i])
                indeksyM1.append(i)
            else:
                mniejszeM2.append(M[1][i])
                indeksyM2.append(i)

        posortowaneM1 = sorted(zip(mniejszeM1,indeksyM1),key=lambda x: (x[0], x[1]))
        posortowaneM2 = sorted(zip(mniejszeM2,indeksyM2),key=lambda x: (x[0], -x[1]),reverse=True)

        _, indeksyPosortowane1 = zip(*posortowaneM1)
        _, indeksyPosortowane2 = zip(*posortowaneM2)

        kolejnosci = indeksyPosortowane1 + indeksyPosortowane2



# Uproszczenie do problemu dwóch maszyn
    if (liczbaMaszyn > 2 and not roznaKolejnosc):
        k = math.ceil(liczbaMaszyn/2)
        M1 = np.sum(M[0:k], axis = 0)
        M2 = np.sum(M[k:],axis = 0) 
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


        
        posortowaneM1 = sorted(zip(mniejszeM1,indeksyM1),key=lambda x: (x[0], x[1]))
        posortowaneM2 = sorted(zip(mniejszeM2,indeksyM2),key=lambda x: (x[0], -x[1]),reverse=True)

        _, indeksyPosortowane1 = zip(*posortowaneM1)
        _, indeksyPosortowane2 = zip(*posortowaneM2)

        kolejnosci = indeksyPosortowane1 + indeksyPosortowane2   


# Różna kolejność na parach maszyn 
    if liczbaMaszyn >2 and roznaKolejnosc:
        k = math.ceil(liczbaMaszyn/2)
        
        if liczbaMaszyn % 2 == 0:
            for j in range(k):
                mniejszeM1 = []
                mniejszeM2 = []

                indeksyM1 = []
                indeksyM2 = []

                for i in range(len(M[0])):
                    if M[2*j][i] <= M[2*j+1][i]:
                        mniejszeM1.append(M[2*j][i])
                        indeksyM1.append(i)
                    else:
                        mniejszeM2.append(M[2*j+1][i])
                        indeksyM2.append(i)

                
                posortowaneM1 = sorted(zip(mniejszeM1,indeksyM1),key=lambda x: (x[0], x[1]))
                posortowaneM2 = sorted(zip(mniejszeM2,indeksyM2),key=lambda x: (x[0], -x[1]),reverse=True)

                print(posortowaneM2)

                _, indeksyPosortowane1 = zip(*posortowaneM1)
                _, indeksyPosortowane2 = zip(*posortowaneM2)

                kolejnosci.append(indeksyPosortowane1 + indeksyPosortowane2)

        else:
            print("Nieparzyście")

    return kolejnosci