import pandas as pd

# Lê o arquivo CSV e guarda numa variável chamada "df" (abreviação de DataFrame)
df = pd.read_csv("dados/PS_20174392719_1491204439457_log.csv")

# Mostra quantas linhas e colunas o dataset tem
print("Formato do dataset (linhas, colunas):", df.shape)

# Mostra o nome de todas as colunas
print("\nColunas disponíveis:")
print(df.columns.tolist())

# Mostra as 5 primeiras linhas, pra gente ver como os dados são
print("\nPrimeiras linhas:")
print(df.head())