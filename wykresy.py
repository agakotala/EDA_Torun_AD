import pandas as pd

df = pd.read_csv("klienci.csv")

duplikaty = df[df.duplicated(keep=False)]
#print(duplikaty)

import matplotlib.pyplot as plt
import seaborn as sns

city_counts = df['miasto'].value_counts()

plt.figure(figsize=(8, 4)) #ustawia rozmiar wykresu, 8 szerosc wykresu, 4 wysokosc wyrkesu w calach
city_counts.plot(kind='bar')
plt.xlabel('miasto')
plt.ylabel('liczba klientów')
plt.title('Liczba klientów w miastach')
plt.xticks(rotation = 45)
plt.tight_layout()
#plt.savefig('wykres_klienci.png')
#plt.show()

