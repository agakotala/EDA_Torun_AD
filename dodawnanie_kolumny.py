import pandas as pd
import numpy as np

df = pd.read_csv("klienci.csv")

np.random.seed(42) #ziarno losowości, wtedy dane losują się takie same zawsze

df["status"] = np.random.choice(["aktywny", 'nieaktywny'], size = len(df))

#mapowanie, zmiana tesktu na wartości
df["status"] = df["status"].map({
    "aktywny": 1,
    "nieaktywny": 0
})

df.to_csv("klienci.csv", index=False)

