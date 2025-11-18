import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("klienci.csv")

city_counts = df['miasto'].value_counts()

plt.figure(figsize = (10,10))
#rysujemy wykres kołowy na podstawie liczby klientów w miastach
plt.pie(
    city_counts,                   #wartości – liczba klientów w miastach
    labels = city_counts.index,    #etykiety – nazwy miast
    autopct='%1.1f%%',             #wyświetlanie procentów z dokładnością do jednego miejsca po przecinku
    startangle=90                  #obracamy wykres, żeby pierwszy segment zaczynał się od godziny 12
)
plt.title('Udział klientów w poszczegolnych maistach')
plt.tight_layout()
plt.savefig("wykres_kolowy_miasta.png",dpi=300)
plt.show()
