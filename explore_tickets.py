import pandas as pd

df = pd.read_csv("data/tickets.csv")

print("Rows and columns:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn types:")
print(df.dtypes)

print("\nTickets per priority:")
print(df["priority"].value_counts())

print("\nTickets per status:")
print(df["status"].value_counts())

print("\nMissing values per column:")
print(df.isna().sum())