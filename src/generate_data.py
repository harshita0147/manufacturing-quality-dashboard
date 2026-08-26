from ucimlrepo import fetch_ucirepo 
import pandas as pd

secom = fetch_ucirepo(id=179)

df = secom.data.original

Y = df["class"]
X = df.drop(columns=["class","timestamp"])

print(X.shape)
print(Y.shape)
print(Y.value_counts())
