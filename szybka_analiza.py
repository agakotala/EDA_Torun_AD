import pandas as pd
df= pd.read_csv("wynagrodzenia.csv")

# print(df.head()) #wyświetla w domyśle 5 pierwszych wierszy
# print(df.info()) #podaje metadane (liczba nie-null, typy kolumn)
# print(df.describe()) #zwraca std - odchylenie standardowe, mean, count - zliacznie, min, max, kawrtyle
# print(df[["wiek", "dochód"]].describe()) #analizuje tylko te dwie kolumny, mozna dodac wiecej, lub mniej, jak jest jedna kolumna do analizy to jeden[], a jak wiecej to [[]]
# print(df.isnull().sum()) #sprawdzenie brakujacych dnaych, sum zlicza brakujace dane
# print(df.tail()) #wyświetla w domyśle 5 ostatnich wierszy

#filtrowanie
wiek_i_dochod = df[['wiek', 'dochód']]
powyzej_30 = df[df['wiek'] > 30]
powyzej_30_kobiety = df[(df['wiek'] > 30) & (df['płeć'] == 'K')] #uyżywamy and, ale kazdy warunek w nawiasie okrągłym

#print(wiek_i_dochod.head())
#print(powyzej_30.head())
#print(powyzej_30_kobiety.head())

sredni_dochod = df.groupby('płeć')['dochód'].mean()

#print(sredni_dochod)

agregaty = df.groupby('płeć').agg({
    'dochód': ['mean', 'median', 'std'], #policz dla kolumny dochod sredia, mediane, odchylenie standardowe
    'wiek': ['min', 'max', 'count'] #policz dla kolumny wiek min, max i liczbe obsrewacji
})

#print(agregaty)

def przydziel_wiek(wiek): #definiujemy funkcję przydzielajaca grupe wiekowa
    if wiek < 30:
        return 'młody' #jesli wiek mniej niz 30 zworc mlody
    elif wiek < 60:
        return 'dorosły' #jesli wiek mniej niz 60 zwroc dorosly
    else:
        return 'senior'

df['wiek_grupa'] = df['wiek'].apply(przydziel_wiek)
print('wiek_grupa = \n' + str(df['wiek_grupa']))
