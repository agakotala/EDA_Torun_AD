import pandas as pd
import numpy as np

klienci = pd.read_csv("klienci.csv")
sprzedaz = pd.read_csv("sprzedaz.csv")

#print(sprzedaz.head(10))

sprzedaz["klient_id"] = np.random.choice(klienci["klient_id"], size=len(sprzedaz))

sprzedaz.to_csv("sprzedaz_z_idklient.csv", index=False)

