import pandas as pd
import random

random.seed(42)

imiona = ["Anna", "Antek", "Jan", "Pola", "Ela", "Jola", "Ewa", "Tomasz", "Julian", "Tadeusz", "Franciszek"]

miasta = ["Warszawa", "Legnica", "Wrocław", "Zielona Góra", "Gdynia", "Adamczycha", "Pcim", "Łódź"]

n = 1000

dane = {
    "imie": [random.choice(imiona) for _ in range(n)],
    "miasto": [random.choice(miasta) for _ in range(n)],
    "dochód": [random.randint(5800, 28500) for _ in range(n)],
    "ma_dzieci": [],
    "liczba_dzieci": [],
    "ma_zwierze": [],
    "jakie_zwierze": []
}

for _ in range(n):
    if random.choice([True, False]):
        dane["ma_dzieci"].append("Tak")
        dane["liczba_dzieci"].append(random.randint(1, 4))
    else:
        dane["ma_dzieci"].append("Nie")
        dane["liczba_dzieci"].append(0)

    if random.choice([True, False]):
        dane["ma_zwierze"].append("Tak")
        dane["jakie_zwierze"].append(random.choice(["pies", "kot", "chomik", "papuga"]))
    else:
        dane["ma_zwierze"].append("Nie")
        dane["jakie_zwierze"].append("brak")

df = pd.DataFrame(dane)

df.to_csv("dane_ludzie.csv", index=False, encoding='utf-8-sig')

print("plik zapisany")

