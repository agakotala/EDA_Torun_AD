import pandas as pd

df = pd.read_csv("klienci.csv")
#wyszukujemy duplikaty w całym DataFrame, duplicated(keep=False) zaznacza wszystkie wiersze, które występują więcej niż raz
duplikaty = df[df.duplicated(keep=False)]
#print(duplikaty)

import matplotlib.pyplot as plt
import seaborn as sns

city_counts = df['miasto'].value_counts() #liczymy, ile razy występuje każde miasto w kolumnie 'miasto', value_counts() zwraca serię z nazwami miast i ich liczbą wystąpień

plt.figure(figsize=(8, 4)) #ustawia rozmiar wykresu, 8 szerosc wykresu, 4 wysokosc wyrkesu w calach
city_counts.plot(kind='bar') #rysujemy wykres słupkowy (bar) na podstawie zliczonych miast
plt.xlabel('miasto') #ustawiamy etykietę osi X
plt.ylabel('liczba klientów') #ustawiamy etykietę osi Y
plt.title('Liczba klientów w miastach') #ustawiamy tytuł
plt.xticks(rotation = 45) #obracamy etykiety na osi X o 45 stopni, żeby były lepiej czytelne
plt.tight_layout() #dopasowujemy elementy wykresu, żeby nic się nie nachodziło na siebie
#plt.savefig('wykres_klienci.png') #zapis wykresu jako png
#plt.show() #pokaz wykres

