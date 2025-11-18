import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'  #ustawienie domyślnej czcionki 

df = pd.read_csv("klienci.csv")
city_counts = df['miasto'].value_counts()
colors = [
    '#ffb3ba',  # pastelowy róż jasny
    '#ffdfba',  # pastelowy pomarańcz jasny
    '#ffffba',  # pastelowy żółty
    '#baffc9',  # pastelowy zielony
    '#bae1ff',  # pastelowy niebieski
    '#e2baff',  # pastelowy fiolet
    '#ffd1dc',  # pastelowy róż 2
    '#ffe5b4',  # pastelowy morelowy
    '#f1f8b0',  # pastelowy limonkowy
    '#c6f5d8',  # pastelowy miętowy
    '#d4eaff',  # pastelowy błękit
    '#e8d4ff',  # pastelowy lawendowy
    '#f7c6c7',  # pastelowy koral
    '#fde2e4',  # pastelowy róż pudrowy
    '#e3f2fd'   # pastelowy błękit jasny
]
plt.figure(figsize = (12,12))
plt.pie(                        #wykres kolowy
    city_counts,
    labels = city_counts.index,            #etykiety – nazwy miast
    colors = colors[:len(city_counts)],        #kolory – bierzemy tyle kolorów, ile mamy miast
    autopct = '%1.1f%%',        #pokazuje procenty z dokładnością do 1 miejsca po przecinku
    startangle = 90,            #początek wykresu ustawiony na godzinę 12 (90 stopni)
    shadow = True,             #dodaje cień pod wykresem dla lepszego efektu 3D
    explode = [0.15] + [0] * (len(city_counts) - 1), 
    #explode – "odciąga" pierwszy kawałek wykresu od reszty
    #0.15 – odległość pierwszego segmentu
    #reszta segmentów ma 0, więc pozostają na miejscu
    textprops = {'fontsize': 12,  #wielkość czcionki etykiet
                 'fontfamily': 'Comic Sans MS'} #krój czcionki etykiet
)
plt.title('Udział klientow wg miast', fontsize = 16, fontweight = 'bold', fontstyle = 'italic',fontfamily = 'Times New Roman') #fontweight bold pogrubienie, fontstyle italic - kursywa
plt.tight_layout()
plt.savefig('wykres_kolowy_pastel_2.png', dpi=300) #zapisujemy wykres do pliku PNG w wysokiej jakości (300 DPI)
plt.show()
