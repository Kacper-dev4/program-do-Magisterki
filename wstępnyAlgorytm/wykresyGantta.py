
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def rysujGantta(maszyny,kolejnosc):
    

    liczba_maszyn = len(maszyny)
    liczba_zadan = len(maszyny[0])
    colors = cm.get_cmap('tab20', liczba_zadan)

    fig, ax = plt.subplots(figsize=(12, 1 + liczba_maszyn * 0.7))

    for i, maszyna in enumerate(maszyny):
        for j, (start, duration) in enumerate(maszyna):
            ax.barh(liczba_maszyn - 1 - i, duration, left=start, height=0.5, color=colors(j))
            ax.text(start + duration / 2, liczba_maszyn - 1 - i, f'Zad {kolejnosc[j]+1}', 
                    va='center', ha='center', color='white', fontsize=8)

    ax.set_yticks(range(liczba_maszyn))
    ax.set_yticklabels([f'Maszyna {i+1}' for i in reversed(range(liczba_maszyn))])
    ax.set_xlabel('Czas')
    ax.set_title('Wykres Gantta')

    # Znalezienie maksymalnego czasu
    max_time = max(start + duration for maszyna in maszyny for (start, duration) in maszyna)
    ax.set_xticks(range(0, int(max_time) + 1, 1))
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()


def rysujGantta2(maszyny,kolejnosc):
    
    k = 0
    pomoc = 0
    liczba_maszyn = len(maszyny)
    liczba_zadan = len(maszyny[0])
    colors = cm.get_cmap('tab20', liczba_zadan)

    fig, ax = plt.subplots(figsize=(12, 1 + liczba_maszyn * 0.7))

    for i, maszyna in enumerate(maszyny):
        for j, (start, duration) in enumerate(maszyna):
            ax.barh(liczba_maszyn - 1 - i, duration, left=start, height=0.5, color=colors(j))
            ax.text(start + duration / 2, liczba_maszyn - 1 - i, f'Zad {kolejnosc[k][j]+1}', 
                    va='center', ha='center', color='white', fontsize=8)
        pomoc = pomoc + 1
        if pomoc == 2:
            pomoc = 0
            k = k + 1 
    ax.set_yticks(range(liczba_maszyn))
    ax.set_yticklabels([f'Maszyna {i+1}' for i in reversed(range(liczba_maszyn))])
    ax.set_xlabel('Czas')
    ax.set_title('Wykres Gantta')

    # Znalezienie maksymalnego czasu
    max_time = max(start + duration for maszyna in maszyny for (start, duration) in maszyna)
    ax.set_xticks(range(0, int(max_time) + 1, 1))
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()


def gantt(Mt,kolejnosc):
    poczatek = 0
    maszyny = []
    koniec = []
    koniecNowy = []
    F = []
    liczbaMaszyn = sum(1 for element in Mt if isinstance(element, list))
    liczbaZadan = len(Mt[0])
    
    for i in range(liczbaMaszyn):
      
        maszyna = []
      
        for j in range(liczbaZadan):
            if i == 0:
                maszyna.append((poczatek,Mt[i][kolejnosc[j]]))
                poczatek = poczatek + Mt[i][kolejnosc[j]]
                koniecNowy.append(poczatek)
                F.append(poczatek)
            else:
                if j == 0:
                    maszyna.append((koniec[j],Mt[i][kolejnosc[j]]))
                    poczatek = koniec[j] + Mt[i][kolejnosc[j]]
                    
                    koniecNowy.append(poczatek)
                else:
                    if koniec[j] > poczatek:
                        maszyna.append((koniec[j],Mt[i][kolejnosc[j]]))
                        poczatek = koniec[j] + Mt[i][kolejnosc[j]]
                        koniecNowy.append(poczatek)
                    else:
                        maszyna.append((poczatek,Mt[i][kolejnosc[j]]))
                        poczatek = poczatek + Mt[i][kolejnosc[j]]
                        koniecNowy.append(poczatek)

            if Mt[i][kolejnosc[j]] > 0: 
                F[j] = poczatek
        koniec = koniecNowy
        koniecNowy = []        
        maszyny.append(maszyna)
    print(maszyny)

    rysujGantta(maszyny,kolejnosc)
    Cmax = poczatek
    Fsrd = sum(F)/len(F)
    return Cmax, Fsrd

def gantt2(Mt,kolejnosc):
    k = 0
    pomoc = 0
    poczatek = 0
    maszyny = []
    koniec = []
    koniecNowy = []
    F = []
    liczbaMaszyn = sum(1 for element in Mt if isinstance(element, list))
    liczbaZadan = len(Mt[0])
    
    for i in range(liczbaMaszyn):
      
        maszyna = []
        
        for j in range(liczbaZadan):
            if i == 0:
                maszyna.append((poczatek,Mt[i][kolejnosc[k][j]]))
                poczatek = poczatek + Mt[i][kolejnosc[k][j]]
                koniecNowy.append(poczatek)
                F.append(poczatek)
            else:
                if j == 0:
                    maszyna.append((koniec[j],Mt[i][kolejnosc[k][j]]))
                    poczatek = koniec[j] + Mt[i][kolejnosc[k][j]]
                    
                    koniecNowy.append(poczatek)
                else:
                    if koniec[j] > poczatek:
                        maszyna.append((koniec[j],Mt[i][kolejnosc[k][j]]))
                        poczatek = koniec[j] + Mt[i][kolejnosc[k][j]]
                        koniecNowy.append(poczatek)
                    else:
                        maszyna.append((poczatek,Mt[i][kolejnosc[k][j]]))
                        poczatek = poczatek + Mt[i][kolejnosc[k][j]]
                        koniecNowy.append(poczatek)

            if Mt[i][kolejnosc[k][j]] > 0: 
                F[j] = poczatek
        pomoc = pomoc + 1
        if pomoc == 2:
            pomoc = 0
            k = k + 1
        koniec = koniecNowy
        koniecNowy = []        
        maszyny.append(maszyna)
    print(maszyny)

    rysujGantta2(maszyny,kolejnosc)
    Cmax = poczatek
    Fsrd = sum(F)/len(F)
    
    return Cmax, Fsrd