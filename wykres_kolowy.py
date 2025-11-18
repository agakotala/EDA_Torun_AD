import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("klienci.csv")

city_counts = df['miasto'].value_counts()

plt.figure(figsize = (10,10))
plt.pie(city_counts, labels = city_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Udział klientów w poszczegolnych maistach')
plt.tight_layout()
plt.savefig("wykres_kolowy_miasta.png",dpi=300)
plt.show()