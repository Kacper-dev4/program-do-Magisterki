
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def gantt(Mt,kolejnosc):
    poczatek = 0
    maszyny = []
    koniec = []
    koniecNowy = []
    liczbaMaszyn = sum(1 for element in Mt if isinstance(element, list))
    liczbaZadan = len(Mt[0])
    
    for i in range(liczbaMaszyn):
      
        maszyna = []
      
        for j in range(liczbaZadan):
            if i == 0:
                maszyna.append((poczatek,Mt[i][kolejnosc[j]]))
                poczatek = poczatek + Mt[i][kolejnosc[j]]
                koniecNowy.append(poczatek)
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


        koniec = koniecNowy        
        maszyny.append(maszyna)
    print(maszyny)
    return liczbaMaszyn

# Dane: (start, czas_trwania)
maszyna_1 = [(0, 3), (3, 2), (5, 4), (9, 1), (10, 3), (13, 2), (15, 1), (16, 2)]
maszyna_2 = [(1, 4), (5, 3), (8, 2), (11, 2), (14, 3), (17, 1), (18, 2), (20, 2)]

fig, ax = plt.subplots(figsize=(12, 4))

# Generujemy paletę kolorów - tyle ile zadań na każdej maszynie
colors = cm.get_cmap('tab20', len(maszyna_1))  # paleta dla maszyn 

# Rysujemy zadania na pierwszej maszynie (y=1)
for i, (start, duration) in enumerate(maszyna_1):
    ax.barh(1, duration, left=start, height=0.5, color=colors(i))
    ax.text(start + duration/2, 1, f'Zad {i+1}', va='center', ha='center', color='white')

# Rysujemy zadania na drugiej maszynie (y=0)
for i, (start, duration) in enumerate(maszyna_2):
    ax.barh(0, duration, left=start, height=0.5, color=colors(i))
    ax.text(start + duration/2, 0, f'Zad {i+1}', va='center', ha='center', color='white')

ax.set_yticks([0, 1])
ax.set_yticklabels(['Maszyna 2', 'Maszyna 1'])
ax.set_xlabel('Czas')
ax.set_title('Wykres Gantta z różnymi kolorami zadań')

# Dodanie ticków na osi X co 1 jednostkę
max_time = max(max(start + duration for start, duration in maszyna_1),
               max(start + duration for start, duration in maszyna_2))
ax.set_xticks(range(0, int(max_time) + 1, 1))

plt.show()
