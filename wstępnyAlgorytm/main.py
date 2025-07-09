
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
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

print(indeksyPosortowane1)

print(indeksyPosortowane2)








# Dane: (start, czas_trwania)
maszyna_1 = [(0, 3), (3, 2), (5, 4), (9, 1), (10, 3), (13, 2), (15, 1), (16, 2)]
maszyna_2 = [(1, 4), (5, 3), (8, 2), (11, 2), (14, 3), (17, 1), (18, 2), (20, 2)]

fig, ax = plt.subplots(figsize=(12, 4))

# Generujemy paletę kolorów - tyle ile zadań na każdej maszynie
colors1 = cm.get_cmap('tab20', len(maszyna_1))  # paleta dla maszyny 1
colors2 = cm.get_cmap('tab20', len(maszyna_2))  # paleta dla maszyny 2

# Rysujemy zadania na pierwszej maszynie (y=1)
for i, (start, duration) in enumerate(maszyna_1):
    ax.barh(1, duration, left=start, height=0.5, color=colors1(i))
    ax.text(start + duration/2, 1, f'Zad {i+1}', va='center', ha='center', color='white')

# Rysujemy zadania na drugiej maszynie (y=0)
for i, (start, duration) in enumerate(maszyna_2):
    ax.barh(0, duration, left=start, height=0.5, color=colors2(i))
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
