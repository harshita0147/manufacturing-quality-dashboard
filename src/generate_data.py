from ucimlrepo import fetch_ucirepo 
import pandas as pd

secom = fetch_ucirepo(id=179)

df = secom.data.original

Y = df["class"]
X = df.drop(columns=["class","timestamp"])

print(X.shape)
print(Y.shape)
print(Y.value_counts())

print(X.isna().sum().sum())
print(X.isna().sum().sort_values(ascending=False).head(10))

missing_pct = X.isna().sum()/len(X)
cols_to_drop = missing_pct[missing_pct > 0.5].index

X_clean = X.drop(columns=cols_to_drop)

print(f"dropped {len(cols_to_drop)} columns with more than 50% missing data")
print(X_clean.shape)

X_filled = X_clean.fillna(X_clean.mean())
print(X_filled.isna().sum().sum())

