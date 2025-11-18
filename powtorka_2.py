def kategorie_miast(miasto):
    Duze_Miasta = ["Warszawa", "Kraków", "Gdańsk", "Wrocław"]
    if miasto in Duze_Miasta:
        return "duże miasto"
    elif len(miasto) > 8:
        return "średnie miasto"
    else:
        return "małe miasto"

import pandas as pd
df = pd.read_csv("klienci.csv")
wyniki = {"duże miasto": 0, "średnie miasto": 0, "małe miasto": 0}

for i in range(len(df)):
    miasto = df.loc[i, "miasto"]
    kat = kategorie_miast(miasto)
    wyniki[kat] += 1

#print("podsumowanie klientów wg kategoria_miasta: ")
#print(wyniki)

