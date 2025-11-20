import pandas as pd               #importuje bibliotekę pandas i nadaje jej alias "pd" – służy do pracy z danymi tabelarycznymi (DataFrame)
import matplotlib.pyplot as plt   #importuje moduł pyplot z matplotlib jako "plt" – do tworzenia wykresów
import seaborn as sns             #importuje bibliotekę seaborn jako "sns" – rozszerzenie do ładniejszych wykresów (tu używane do heatmapy)
import numpy as np                #importuje bibliotekę NumPy jako "np" – do obliczeń numerycznych i pracy z tablicami
import matplotlib                 #importuje główny moduł matplotlib – tu używany do ustawień globalnych (rcParams)
import contextlib                 #importuje contextlib – narzędzia do pracy z kontekstami (with), np. redirect_stdout
import locale                     #importuje bibliotekę locale – pozwala ustawić lokalne formatowanie liczb / dat / walut
from datetime import datetime     #importuje klasę datetime – do pracy z datą i czasem

dataa = datetime.now().strftime("%Y-%m-%d")  #pobiera bieżącą datę i zamienia ją na tekst w formacie RRRR-MM-DD, zapisuje do zmiennej "dataa"
matplotlib.rcParams['axes.formatter.use_locale'] = True  #ustawia w matplotlib, aby używać ustawień locale przy formatowaniu osi (np. separator tysięcy)
locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8')           #ustawia lokalizację na polską (formatowanie liczb, dat, itp.)


#przykład konfiguracji plki csv
#df = pd.read_csv('dane_csv.csv', delimiter=None, header='infer', index_col=None, usecols=None, dtype=None, engine=None, true_values=None, false_values=None, skipinitialspace=True, skiprows=None, nrows=None, na_filter=True, skip_blank_lines=True, parse_dates=['data'], data_format=None, dayfirst=False, thousands=None, decimal='.', lineterminator=None, quotechar="", doublequote=True, comment='#', encoding=None, encoding_errors='strict', on_bad_lines='error')
def main(): #definiuje funkcję główną programu o nazwie "main"

    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-31/beers.csv" #zmienna "url" – adres do pliku CSV z danymi o piwach w repozytorium GitHub

    try:  #rozpoczyna blok try – próba wykonania kodu, który może rzucić wyjątek
        df = pd.read_csv(url)  #próbuje wczytać dane z adresu URL do obiektu DataFrame o nazwie df
        print('dane pobrane')  #jeśli wczytanie się uda, wypisuje komunikat, że dane zostały pobrane
    except Exception as e:  #jeśli wystąpi jakikolwiek błąd, przechodzi do bloku except i łapie wyjątek jako "e"
        print(f'Błąd {e}')  #wypisuje komunikat o błędzie wraz z treścią wyjątku
        print('Używam danych zapasowych')  #informuje, że zamiast danych z internetu użyje danych zapasowych
        data = {  #tworzy słownik "data" – przykładowe dane o piwach w formie słownika list
            'nazwa': ['IPA', 'IPA', 'Lager', 'Stout', 'Pilsner', 'Wheat', 'Porter', 'Bock', 'Ale'],  #lista nazw piw
            'alkohol': [6.5, 6.5, 5.0, 7.2, 4.8, 5.2, 5.8, 5.5, 6.8],                                #lista zawartości alkoholu
            'goryczka': [65, 65, np.nan, 45, 30, 15, 40, 35, 25],                                    #lista IBU (goryczki), z jedną wartością brakującą (np.nan)
            'ocena': [4.2, 4.2, 3.8, 4.5, 3.9, 3.7, 4.1, 4.0, 4.3],                                  #lista ocen piw
            'styl': ['IPA', 'IPA', 'Lager', 'Ciemne', 'Lager', np.nan, 'Ciemne', 'Jasne', 'Ciemne']  #lista stylów piw, z jedną wartością brakującą
        }
        df = pd.DataFrame(data)  #tworzy DataFrame df z danych zapasowych ze słownika "data"
    print(df)      #wypisuje całą tabelę df na ekran
    print(dataa)   #wypisuje datę bieżącą zapisaną w zmiennej dataa
    #podstawowe info
    print('\n' + '='*50)
    print('PODSTAWOWE INFORMACJE')
    print('='*50)

    print(f'Wymiary danych: {df.shape}')   #wypisuje krotkę (liczba wierszy, liczba kolumn) DataFrame df
    print(f'Liczba wierszy: {df.shape[0]}')  #wypisuje liczbę wierszy (pierwszy element df.shape)
    print(f'Liczba kolumn: {df.shape[1]}')   #wypisuje liczbę kolumn (drugi element df.shape)


    print('\n' + '='*50)
    print('PODGLĄD DANYCH')
    print('='*50)

    print('Pierwsze 5 piw: ')    #tekst informujący, że za chwilę pokaże pierwsze wiersze
    print(df.head())             #wypisuje pierwsze 5 wierszy DataFrame (domyślnie head(5))
    print('5 ostatnich piw: ')   #tekst informujący o wyświetleniu ostatnich wierszy
    print(df.tail())             #wypisuje ostatnie 5 wierszy DataFrame (domyślnie tail(5))

    print('\n' + '='*50)
    print('TYPY DANYCH')
    print('='*50)

    print(f'\n{df.info()}')      #wyświetla informacje o DataFrame: liczba wierszy, kolumn, typy danych, liczby niepustych wartości

    #statystyki numeryczne
    print('\n' + '='*50)        
    print('STATYSTYKI NUMERYCZNE')  
    print('='*50)               

    kolumny_numeryczne = df.select_dtypes(include='number').columns  #wybiera nazwy kolumn o typach numerycznych i zapisuje je w zmiennej
    if len(kolumny_numeryczne) > 0:  #sprawdza, czy istnieje przynajmniej jedna kolumna numeryczna
        print('Statystyki dla cech numerycznych: ')  #informacja tekstowa
        print(df[kolumny_numeryczne].describe())     #wypisuje opisowe statystyki (min, max, średnia, kwartyle) dla kolumn numerycznych
    else:                                            #jeśli nie ma kolumn numerycznych
        print('Brak kolumn numerycznych w danych')   #informuje o braku kolumn numerycznych

    #statystyki kategoryczne
    print('\n' + "="*50)          
    print("STATYSTYKI KATEGORYCZNE")  
    print('='*50)                 

    kolumny_tekstowe = df.select_dtypes(include='object').columns  #wybiera nazwy kolumn tekstowych (typ 'object')
    if len (kolumny_tekstowe) > 0:  #jeśli istnieje choć jedna kolumna tekstowa
        for kolumna in kolumny_tekstowe:  #iteruje po każdej kolumnie tekstowej
            print(f'\nKolumna: {kolumna}')                         #wypisuje nazwę aktualnej kolumny
            print(f'Unikalne wartości: {df[kolumna].unique()}')    #wypisuje tablicę unikalnych wartości z tej kolumny
            print(f'Liczba unikalnych wartości: {len(df[kolumna].unique())}')  #wypisuje liczbę unikalnych wartości
            print('3 najczęstsze wartości: ')                      #zapowiedź wyświetlenia najczęstszych wartości
            print(df[kolumna].value_counts().head(3))              #wypisuje 3 najczęściej występujące wartości z tej kolumny
    else:  # jeśli nie znaleziono kolumn tekstowych
        print("Brak kolumn kategorycznych w danych")  #informuje o braku kolumn kategorycznych

    #brakujące wartości
    print('\n' + '='*50)         
    print("BRAKUJĄCE WARTOŚCI")  
    print("="*50)                

    brakujace = df.isna().sum()           #tworzy serię z liczbą braków (NaN) w każdej kolumnie
    if brakujace.sum() > 0:               #jeżeli suma braków we wszystkich kolumnach jest większa od 0
        print('Kolumny z brakującymi wartościami: ')  #informuje, że poniżej wypisze kolumny z brakami
        for kolumna in df.columns:                   #iteruje po wszystkich kolumnach DataFrame
            if df[kolumna].isna().sum() > 0:         #sprawdza, czy w danej kolumnie są jakieś braki
                braki_liczbowo = df[kolumna].isnull().sum()    #liczy dokładną liczbę braków w tej kolumnie
                braki_procentowo = (braki_liczbowo / len(df)) * 100  #przelicza liczbę braków na procent wierszy
                print(f' {kolumna}: {braki_liczbowo} ({braki_procentowo:.2f}%)')  #wypisuje nazwę kolumny, liczbę braków i procent

    print("\n" + "="*50)         
    print("TWORZENIE WYKRESÓW")  
    print("="*50)               

    if 'alkohol' in df.columns and False:  #warunek: jeśli jest kolumna 'alkohol' ORAZ stała False (czyli blok jest zawsze wyłączony)
        plt.figure(figsize = (10, 6))      #tworzy nową figurę o rozmiarze 10x6 cali

        plt.subplot(1, 3, 1)               #tworzy 1-szy z 3 podwykresów w jednym wierszu
        plt.title('Rozkład zawartości alkoholu')      #tytuł pierwszego podwykresu
        plt.xlabel('Zawartość alko w (%)')            #etykieta osi X
        plt.ylabel('Liczba piw')                      #etykieta osi Y
        plt.tight_layout()                            #automatycznie dopasowuje elementy wykresu, aby się nie nachodziły
        plt.hist(df.alkohol)                          #rysuje histogram zawartości alkoholu

        plt.subplot(1, 3, 2)                          #przełącza się na 2-gi podwykres
        plt.title('Rozkład zawrtości alkoholu')       #tytuł drugiego podwykresu
        plt.xlabel("Zawartość alko w (%)")            #etykieta osi X
        plt.ylabel('Liczba piw')                      #etykieta osi Y
        plt.tight_layout()                            #dopasowanie układu
        df['alkohol'].hist(bins=10, color='lightblue', edgecolor='black')  #histogram z 10 binami, kolorem słupków i obramowaniem

        plt.subplot(1, 3, 3)                          #przełącza na 3-ci podwykres
        df.boxplot(column='alkohol', grid=False)      #rysuje wykres pudełkowy (boxplot) dla kolumny 'alkohol'
        plt.title("boxplot: Zawartość alkoholu")      #tytuł trzeciego podwykresu
        # plt.savefig('boxplot.png')                  #zapis wykresu do pliku
        # plt.show()                                  #wyświetlenie wykresu na ekranie
        # wykres 2 z ocena                            #komentarz: pomysł na drugi wykres z oceną

    if 'ocena' in df.columns and False:  #jeśli istnieje kolumna 'ocena' i dodatkowy warunek False (blok wyłączony)
        plt.figure(figsize = (8, 5))                             #nowa figura 8x5
        df['ocena'].hist(bins=8, color='lightgreen', edgecolor='black', alpha=0.7)  #histogram ocen z 8 binami
        plt.title('Rozkład oceny piw')                           #tytuł
        plt.xlabel('Ocena w skali 1 - 5)')                       #etykieta osi X
        plt.ylabel('Liczba piw')                                #etykieta osi Y
        plt.grid(axis='y', alpha=0.3)                            #włącza siatkę poziomą z przezroczystością 0.3
        plt.show()                                               #pokazuje wykres

    if 'alkohol' in df.columns and 'ocena' in df.columns and False:  #jeśli są kolumny 'alkohol' i 'ocena' oraz warunek False
        plt.figure(figsize = (8, 6))                                #nowa figura 8x6
        plt.scatter(df['alkohol'], df['ocena'], alpha = 0.6, s=60, color='purple')  #wykres punktowy (scatter) alkohol vs ocena
        plt.title('Zależność między zawrtością alkoholu, a oceną')                  #tytuł wykresu
        plt.xlabel('Zawartość alko w (%)')                           #etykieta osi X
        plt.ylabel('Ocena')                                          #etykieta osi Y
        plt.grid(True, alpha = 0.3, linestyle = '--', linewidth = 2) #włącza siatkę o zadanym stylu

        #linia trendu, przybliżona prosta, która najbardziej pasuje do punktów
        z = np.polyfit(df['alkohol'], df['ocena'], 1)  #dopasowuje prostą (wielomian stopnia 1) do danych (x=alkohol, y=ocena)
        p = np.poly1d(z)                               #tworzy obiekt wielomianu na podstawie współczynników z
        plt.plot(df['alkohol'], p(df['alkohol']), "r-", alpha=0.8)  #rysuje linię trendu na wykresie punktowym
        plt.show()                                      #wyświetla wykres

    if 'styl' in df.columns and False:  #jeśli jest kolumna 'styl' i dodatkowy warunek False (blok wyłączony)
        plt.figure(figsize = (10, 6))                            #nowa figura 10x6
        df['styl'].value_counts().plot(kind='bar', color = 'orange', edgecolor = 'black')  #wykres słupkowy popularności stylów piwa
        plt.title('Popularność stylów piw')                       #tytuł wykresu
        plt.xlabel('Styl piwa')                                   #etykieta osi X
        plt.ylabel('Liczba piw')                                  #etykieta osi Y
        plt.xticks(rotation = 45)                                 #obraca etykiety osi X o 45 stopni
        plt.grid(axis='y', alpha = 0.3)                           #siatka pozioma dla osi Y
        plt.tight_layout()                                        #dopasowanie elementów wykresu
        plt.show()                                                #wyświetlenie wykresu

    #macierz korelacji
    if len(kolumny_numeryczne) >= 2 and False:  #jeśli są co najmniej dwie kolumny numeryczne oraz warunek False (blok wyłączony)
        plt.figure(figsize = (8, 6))                     #nowa figura 8x6
        macierz_korelacji = df[kolumny_numeryczne].corr()  #oblicza macierz korelacji między kolumnami numerycznymi
        sns.heatmap(macierz_korelacji, annot=True, cmap="rocket", center=0)  #rysuje heatmapę korelacji z wartościami w komórkach
        plt.title('Korelacje między ceachami numerycznymi')  #tytuł wykresu
        plt.tight_layout()                                   #dopasowuje układ
        plt.show()                                           #wyświetla wykres

    #analiza duplikatów
    print("\n" + "="*50)            
    print("ANALIZA DUPLIKATÓW")     
    print("="*50)                   

    duplikaty = df.duplicated()     #tworzy serię bool wskazującą, które wiersze są zduplikowane (True = duplikat)
    if duplikaty.sum() > 0:         #jeśli liczba duplikatów (sumowanie True jako 1) jest większa od 0
        print(f'Znaleziono {duplikaty.sum()} zduplikowanych wierszy')  #wypisuje liczbę znalezionych duplikatów
        print('zduplikowane wiersze: ')                               #tekst informacyjny
        print(df[duplikaty])                                          #wypisuje tylko te wiersze, które są duplikatami
    else:                           #jeśli nie znaleziono duplikatów
        print('Brak duplikatów')    #informuje, że nie ma duplikatów

    #czyszczenie danych
    print("\n" + "="*50)                     
    print("PROPOZYCJE CZYSZCZENIA DANYCH")   
    print("="*50)                            

    if 'goryczka' in df.columns and df['goryczka'].isnull().sum() > 0:  #jeśli istnieje kolumna 'goryczka' i są w niej braki
        median_goryczka = df.groupby('styl')['goryczka'].transform('median')  #oblicza medianę goryczki w grupach wg 'styl' i rozciąga do pełnej długości serii
        df['gorczyka_uzupelniona'] = df['goryczka'].fillna(median_goryczka)   #tworzy nową kolumnę, gdzie braki goryczki są uzupełnione medianą z danego stylu
        print(f"Uzupełniono {df['goryczka'].isnull().sum()} brakujących wartosci goryczki")  
        # UWAGA: ten print liczy już po uzupełnieniu (więc zwykle będzie 0) – pokazuje ile braków jest w kolumnie 'goryczka' po operacji

    #usuwanie duplikatów
    if duplikaty.sum() > 0:                         #jeśli były znalezione duplikaty
        df_cleaned = df.drop_duplicates()           #tworzy nowy DataFrame df_cleaned bez zduplikowanych wierszy
        print(f'Usunięto {duplikaty.sum()} duplikatów')  # wypisuje, ile duplikatów usunięto
    # else:
        # df_cleaned = df.copy()                    #można by skopiować df, jeśli nie ma duplikatów

    # kategoryzacja piw
    df_cleaned["kategoria_alkohol"] = pd.cut(              #dodaje nową kolumnę "kategoria_alkohol" w df_cleaned
        df_cleaned["alkohol"],                             #kolumna, która ma zostać pokategoryzowana – zawartość alkoholu
        bins=[0, 5, 6.5, 10],                              #granice przedziałów (0–5, 5–6.5, 6.5–10)
        labels=["lekki", "średnie", "mocne"]               #etykiety kategorii odpowiadające przedziałom
    )
    print("\nKategoria alkoholowe:")                       #nagłówek sekcji kategoryzacji
    print(df_cleaned["kategoria_alkohol"].value_counts())  #wypisuje, ile piw jest w każdej kategorii alkoholu
    print(df_cleaned)                                      #wypisuje cały DataFrame po czyszczeniu i kategoryzacji

    # podsumowanie analizy
    print("\n" + "="*50)                 
    print("PODSUMOWANIE ANALIZY")       
    print("="*50)                       

    print("Analiza EDA zakończona pomyślnie!")             #komunikat o zakończeniu eksploracyjnej analizy danych
    print(f'Przeanalizowano {len(df)} piw')                #wypisuje, ile wierszy (piw) analizowano w oryginalnym df
    print(f'Liczba cech: {len(df.columns)}')               #wypisuje, ile kolumn (cech) zawiera DataFrame

    if len(kolumny_numeryczne) > 0:                        #jeśli były cechy numeryczne
        print("znaleziono cechy numeryczne:", list(kolumny_numeryczne))  #wypisuje listę ich nazw
    if len(kolumny_tekstowe) > 0:                          #jeśli były cechy kategoryczne (tekstowe)
        print("znaleziono cechy kategoryczne:", list(kolumny_tekstowe))  #wypisuje listę ich nazw
    if 'ocena' in df.columns and 'nazwa' in df.columns:    #jeśli istnieją kolumny 'ocena' i 'nazwa'
        print('\nTop 3 najwyżej oceniane piwa')            #nagłówek sekcji top 3 piw
        najlepsze = df.nlargest(3, 'ocena')[['nazwa', 'ocena']]  #wybiera 3 wiersze z najwyższą oceną i tylko kolumny nazwa + ocena
        print(najlepsze)                                   #wypisuje te piwa
    if 'alkohol' in df.columns and 'nazwa' in df.columns:  #jeśli istnieją kolumny 'alkohol' i 'nazwa'
        print("\n3 piwa z największą zawartością alkoholu:")  #nagłówek sekcji o najmocniejszych piwach
        mocne = df.nlargest(3, 'alkohol')[['nazwa', 'alkohol']]  # wybiera 3 piwa o największej zawartości alkoholu
        print(mocne)                                      #wypisuje te piwa
    print("\n" + "="*50)                                  #końcowy separator
    pass                                                  #instrukcja "nic nie rób" 
    
if __name__ == "__main__":  #ten blok uruchomi się tylko wtedy, gdy plik jest uruchamiany bezpośrednio (nie importowany jako moduł)
    with open("raport_analiza_piw.txt", 'w', encoding = "utf-8") as f:  #otwiera plik tekstowy do zapisu, z kodowaniem UTF-8, jako zmienną f
        with contextlib.redirect_stdout(f):  #przekierowuje standardowe wyjście (print) do pliku f wewnątrz tego bloku
            main()                           #wywołuje funkcję main(), a wszystkie printy trafią do pliku "raport_analiza_piw.txt"










