import pandas as pd

# Extract: lê o CSV (repetimos essa etapa aqui pra esse arquivo funcionar sozinho)
df = pd.read_csv("dados/PS_20174392719_1491204439457_log.csv")

# 1. Verifica se existem valores nulos em alguma coluna
print("Valores nulos por coluna:")
print(df.isnull().sum())

# 2. Remove colunas que não vamos usar na análise
df = df.drop(columns=["nameOrig", "nameDest", "isFlaggedFraud"])

# 3. Cria uma coluna nova: nossa própria regra de suspeita
df["flag_suspeita"] = (
    (df["oldbalanceOrg"] > 0) &
    (df["newbalanceOrig"] == 0) &
    (df["amount"] == df["oldbalanceOrg"])
).astype(int)

# Mostra quantas transações nossa regra sinalizou
print("\nTransações sinalizadas pela nossa regra:")
print(df["flag_suspeita"].value_counts())

# Compara com a coluna oficial isFraud, só pra referência
print("\nTransações realmente fraudulentas (isFraud):")
print(df["isFraud"].value_counts())

print("\nPrimeiras linhas após transformação:")
print(df.head())