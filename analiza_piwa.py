import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib
import contextlib
import locale
from datetime import datetime

dataa = datetime.now().strftime("%Y-%m-%d")
matplotlib.rcParams['axes.formatter.use_locale'] = True
locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8')

#przykład konfiguracji plki csv
#df = pd.read_csv('dane_csv.csv', delimiter=None, header='infer', index_col=None, usecols=None, dtype=None, engine=None, true_values=None, false_values=None, skipinitialspace=True, skiprows=None, nrows=None, na_filter=True, skip_blank_lines=True, parse_dates=['data'], data_format=None, dayfirst=False, thousands=None, decimal='.', lineterminator=None, quotechar="", doublequote=True, comment='#', encoding=None, encoding_errors='strict', on_bad_lines='error')
def main():

    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-31/beers.csv"

    try:
        df = pd.read_csv(url) #skrobuj wczytac dane z url
        print('dane pobrane') #jesli sie uda uda to wysweitl
    except Exception as e:
        print(f'Błąd {e}')
        print('Używam danych zapasowych')
        data = {
            'nazwa': ['IPA', 'IPA', 'Lager', 'Stout', 'Pilsner', 'Wheat', 'Porter', 'Bock', 'Ale'],
            'alkohol': [6.5, 6.5, 5.0, 7.2, 4.8, 5.2, 5.8, 5.5, 6.8],
            'goryczka': [65, 65, np.nan, 45, 30, 15, 40, 35, 25],
            'ocena': [4.2, 4.2, 3.8, 4.5, 3.9, 3.7, 4.1, 4.0, 4.3],
            'styl': ['IPA', 'IPA', 'Lager', 'Ciemne', 'Lager', np.nan, 'Ciemne', 'Jasne', 'Ciemne']
        }
        df = pd.DataFrame(data)
    print(df)
    print(dataa)
    #podstawowe info
    print('\n' + '='*50)
    print('PODSTAWOWE INFORMACJE')
    print('='*50)

    print(f'Wymiary danych: {df.shape}') #zwraca krotke liczba wieszy i kolumn
    print(f'Liczba wierszy: {df.shape[0]}') #zwraca liczbe wierszy w tabeli (rekordow)
    print(f'Liczba kolumn: {df.shape[1]}') #zwraca liczbe kolumn

    print('\n' + '='*50)
    print('PODGLĄD DANYCH')
    print('='*50)

    print('Pierwsze 5 piw: ')
    print(df.head())
    print('5 ostatnich piw: ')
    print(df.tail())

    print('\n' + '='*50)
    print('TYPY DANYCH')
    print('='*50)

    print(f'\n{df.info()}')  #df.info wypisze info o kazdej kolumnie: typy, niepuste kol, nazwe kol

    #statystyki numeryczne
    print('\n' + '='*50)
    print('STATYSTYKI NUMERYCZNE')
    print('='*50)

    kolumny_numeryczne = df.select_dtypes(include='number').columns
    if len(kolumny_numeryczne) > 0: #sprawdzamy czy jest przynajmniej jedna kolumna numeryczna
        print('Statystyki dla cech numerycznych: ')
        print(df[kolumny_numeryczne].describe())
    else:
        print('Brak kolumn numerycznych w danych')

    #statystyki kategoryczne

    print('\n' + "="*50)
    print("STATYSTYKI KATEGORYCZNE")
    print('='*50)

    kolumny_tekstowe = df.select_dtypes(include='object').columns
    if len (kolumny_tekstowe) > 0: #jesli jest jakakolwiek kolumna tekstowa
        for kolumna in kolumny_tekstowe:
            print(f'\nKolumna: {kolumna}')
            print(f'Unikalne wartości: {df[kolumna].unique()}')
            print(f'Liczba unikalnych wartości: {len(df[kolumna].unique())}')
            print('3 najczęstsze wartości: ')
            print(df[kolumna].value_counts().head(3))
    else:
        print("Brak kolumn kategorycznych w danych")
    #brakujące wartości
    print('\n' + '='*50)
    print("BRAKUJĄCE WARTOŚCI")
    print("="*50)

    brakujace = df.isna().sum()
    if brakujace.sum() > 0:     #jesli suma brakow we wszystkich kolumnach jest wieksza niz 0
        print('Kolumny z brakującymi wartościami: ')
        for kolumna in df.columns:      #przejdz po kazdej kolumnie
            if df[kolumna].isna().sum() > 0:    #czy w danej kolumnie jest jakiś brak (co namnjiej 1)
                braki_liczbowo = df[kolumna].isnull().sum() #liczy ile dokladnie brakow jest
                braki_procentowo = (braki_liczbowo / len(df)) * 100 #jaki procent wszytskich wierszy to braki
                print(f' {kolumna}: {braki_liczbowo} ({braki_procentowo:.2f}%)')

    print("\n" + "="*50)
    print("TWORZENIE WYKRESÓW")
    print("="*50)

    if 'alkohol' in df.columns and False:
        plt.figure(figsize = (10, 6))

        plt.subplot(1, 3, 1)
        plt.title('Rozkład zawartości alkoholu')
        plt.xlabel('Zawartość alko w (%)')
        plt.ylabel('Liczba piw')
        plt.tight_layout()
        plt.hist(df.alkohol)

        plt.subplot(1, 3, 2)
        plt.title('Rozkład zawrtości alkoholu')
        plt.xlabel("Zawartość alko w (%)")
        plt.ylabel('Liczba piw')
        plt.tight_layout()
        df['alkohol'].hist(bins=10, color='lightblue', edgecolor='black')

        plt.subplot(1, 3, 3)
        df.boxplot(column='alkohol', grid=False)
        plt.title("boxplot: Zawartość alkoholu")
        #plt.savefig('boxplot.png')
        #plt.show()
        #wykres 2 z ocena
    if 'ocena' in df.columns and False:
        plt.figure(figsize = (8, 5))
        df['ocena'].hist(bins=8, color='lightgreen', edgecolor='black', alpha=0.7)
        plt.title('Rozkład oceny piw')
        plt.xlabel('Ocena w skali 1 - 5)')
        plt.ylabel('Liczba piw')
        plt.grid(axis='y', alpha=0.3)
        plt.show()

    if 'alkohol' in df.columns and 'ocena' in df.columns and False:
        plt.figure(figsize = (8, 6))
        plt.scatter(df['alkohol'], df['ocena'], alpha = 0.6, s=60, color='purple')
        plt.title('Zależność między zawrtością alkoholu, a oceną')
        plt.xlabel('Zawartość alko w (%)')
        plt.ylabel('Ocena')
        plt.grid(True, alpha = 0.3, linestyle = '--', linewidth = 2)

        #linia trednu, przyblizona prosta, ktora najbardziej pasuje do pnktow
        z = np.polyfit(df['alkohol'], df['ocena'], 1)
        p = np.poly1d(z)
        plt.plot(df['alkohol'], p(df['alkohol']), "r-", alpha=0.8)
        plt.show()

    if 'styl' in df.columns and False:
        plt.figure(figsize = (10, 6))
        df['styl'].value_counts().plot(kind='bar', color = 'orange', edgecolor = 'black')
        plt.title('Popularność stylów piw')
        plt.xlabel('Styl piwa')
        plt.ylabel('Liczba piw')
        plt.xticks(rotation = 45)
        plt.grid(axis='y', alpha = 0.3)
        plt.tight_layout()
        plt.show()
#macierz korelacji
    if len(kolumny_numeryczne) >= 2 and False:
        plt.figure(figsize = (8, 6))
        macierz_korelacji = df[kolumny_numeryczne].corr()
        sns.heatmap(macierz_korelacji, annot=True, cmap="rocket", center=0)
        plt.title('Korelacje między ceachami numerycznymi')
        plt.tight_layout()
        plt.show()

#analiza duplikatów
    print("\n" + "="*50)
    print("ANALIZA DUPLIKATÓW")
    print("="*50)

    duplikaty = df.duplicated()
    if duplikaty.sum() > 0:
        print(f'Znaleziono {duplikaty.sum()} zduplikowanych wierszy')
        print('zduplikowane wiersze: ')
        print(df[duplikaty])
    else:
        print('Brak duplikatów')

    #czyszczenie danych

    print("\n" + "="*50)
    print("PROPOZYCJE CZYSZCZENIA DANYCH")
    print("="*50)
    if 'goryczka' in df.columns and df['goryczka'].isnull().sum() > 0:
        median_goryczka = df.groupby('styl')['goryczka'].transform('median')
        df['gorczyka_uzupelniona'] = df['goryczka'].fillna(median_goryczka)
        print(f'Uzupełniono {df['goryczka'].isnull().sum()} brakujących wartosci goryczki')
#usuwanie duplikatów
    if duplikaty.sum() > 0:
        df_cleaned = df.drop_duplicates()
        print(f'Usunięto {duplikaty.sum()} duplikatów')
    #else:
        #df_cleaned = df.copy()

    # kategoryzacja piw
    df_cleaned["kategoria_alkohol"] = pd.cut(df_cleaned["alkohol"],
                                             bins=[0, 5, 6.5, 10],
                                             labels=["lekki", "średnie", "mocne"])
    print("\nKategoria alkoholowe:")
    print(df_cleaned["kategoria_alkohol"].value_counts())
    print(df_cleaned)

#podsumowanie analizy
    print("\n" + "="*50)
    print("PODSUMOWANIE ANALIZY")
    print("="*50)

    print("Analiza EDA zakończona pomyślnie!")
    print(f'Przeanalizowano {len(df)} piw')
    print(f'Liczba cech: {len(df.columns)}')

    if len(kolumny_numeryczne) > 0:
        print("znaleziono cechy numeryczne:", list(kolumny_numeryczne))
    if len(kolumny_tekstowe) > 0:
        print("znaleziono cechy kategoryczne:", list(kolumny_tekstowe))
    if 'ocena' in df.columns and 'nazwa' in df.columns:
        print('\nTop 3 najwyżej oceniane piwa')
        najlepsze = df.nlargest(3, 'ocena')[['nazwa', 'ocena']]
        print(najlepsze)
    if 'alkohol' in df.columns and 'nazwa' in df.columns:
        print("\n3 piwa z największą zawartością alkoholu:")
        mocne = df.nlargest(3, 'alkohol')[['nazwa', 'alkohol']]
        print(mocne)
    print("\n" + "="*50)
    pass
if __name__ == "__main__":
    with open("raport_analiza_piw.txt", 'w', encoding = "utf-8") as f:
        with contextlib.redirect_stdout(f):
            main()