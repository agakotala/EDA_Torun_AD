import pandas as pd
import numpy as np

df = pd.read_csv("klienci.csv")

np.random.seed(42) #ziarno losowości, wtedy dane losują się takie same zawsze

#tworzymy nową kolumnę 'status' w DataFrame
#wartość w tej kolumnie jest losowana dla każdego wiersza
#np.random.choice wybiera losowo "aktywny" lub "nieaktywny"
#size = len(df) oznacza, że losujemy tyle wartości, ile wierszy ma DataFrame
df["status"] = np.random.choice(["aktywny", 'nieaktywny'], size=len(df))

#mapowanie wartości tekstowych na wartości liczbowe
#'aktywny' zamieniamy na 1
#'nieaktywny' zamieniamy na 0
#metoda .map() działa na każdej wartości w kolumnie
df["status"] = df["status"].map({
    "aktywny": 1,
    "nieaktywny": 0
})

#zapisujemy DataFrame do pliku CSV o nazwie 'klienci.csv'
#index=False oznacza, że nie zapisujemy indeksów wierszy
df.to_csv("klienci.csv", index=False)

