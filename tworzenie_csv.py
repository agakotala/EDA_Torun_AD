import pandas as pd
import random


#ustawiamy ziarno generatora losowości
#dzięki temu wyniki losowania będą powtarzalne przy każdym uruchomieniu
random.seed(42)
#lista możliwych imion
imiona = ["Anna", "Antek", "Jan", "Pola", "Ela", "Jola", "Ewa", "Tomasz", "Julian", "Tadeusz", "Franciszek"]
#lista możliwych miast
miasta = ["Warszawa", "Legnica", "Wrocław", "Zielona Góra", "Gdynia", "Adamczycha", "Pcim", "Łódź"]
#liczba rekordów (wierszy), które chcemy wygenerować
n = 1000
#tworzymy słownik, który będzie podstawą DataFrame
#początkowo generujemy dane dla pól imie, miasto i dochód
#pozostałe kolumny uzupełnimy później w pętli
dane = {
    "imie": [random.choice(imiona) for _ in range(n)],        #losowe imię z listy
    "miasto": [random.choice(miasta) for _ in range(n)],        #losowe miasto z listy
    "dochód": [random.randint(5800, 28500) for _ in range(n)],    #losowy dochód od 5800 do 28500
    "ma_dzieci": [],            #na razie puste — wypełnimy pętlą
    "liczba_dzieci": [],
    "ma_zwierze": [],
    "jakie_zwierze": []
}
#pętla generująca dane o posiadaniu dzieci i zwierząt
for _ in range(n):
    #losujemy informację, czy osoba ma dzieci
    if random.choice([True, False]):
        dane["ma_dzieci"].append("Tak")    #ma dzieci
        dane["liczba_dzieci"].append(random.randint(1, 4)) #liczba dzieci od 1 do 4
    else:
        dane["ma_dzieci"].append("Nie") #brak dzieci
        dane["liczba_dzieci"].append(0) #wtedy liczba dzieci = 0
    #losujemy informację, czy osoba ma zwierzę
    if random.choice([True, False]):
        dane["ma_zwierze"].append("Tak") #ma zwierzę
        dane["jakie_zwierze"].append(random.choice(["pies", "kot", "chomik", "papuga"]))
    else:
        dane["ma_zwierze"].append("Nie") #nie ma zwierzęcia
        dane["jakie_zwierze"].append("brak") #nie ma zwierzęcia

df = pd.DataFrame(dane)

df.to_csv("dane_ludzie.csv", index=False, encoding='utf-8-sig')
#zapis danych do pliku CSV
#index=False — nie zapisujemy indeksów w pliku
#encoding='utf-8-sig' — aby polskie znaki wyświetlały się poprawnie
print("plik zapisany")

