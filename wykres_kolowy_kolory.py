import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'

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
plt.pie(
    city_counts,
    labels = city_counts.index,
    colors = colors[:len(city_counts)],
    autopct = '%1.1f%%',
    startangle = 90,
    shadow = True,
    explode = [0.15] + [0] * (len(city_counts) - 1),
    textprops = {'fontsize': 12, 'fontfamily': 'Comic Sans MS'}
)
plt.title('Udział klientow wg miast', fontsize = 16, fontweight = 'bold', fontstyle = 'italic',fontfamily = 'Times New Roman') #fontweight bold pogrubienie, fontstyle italic - kursywa
plt.tight_layout()
plt.savefig('wykres_kolowy_pastel_2.png', dpi=300)
plt.show()
