import pandas as pd
import sqlite3

# --- Extract ---
df = pd.read_csv("dados/PS_20174392719_1491204439457_log.csv")

# --- Transform ---
df = df.drop(columns=["nameOrig", "nameDest", "isFlaggedFraud"])

df["flag_suspeita"] = (
    (df["oldbalanceOrg"] > 0) &
    (df["newbalanceOrig"] == 0) &
    (df["amount"] == df["oldbalanceOrg"])
).astype(int)

# --- Load ---
# Cria (ou conecta a) um banco de dados SQLite chamado pipeline.db
conexao = sqlite3.connect("pipeline.db")

# Salva o DataFrame como uma tabela chamada "transacoes" dentro do banco
df.to_sql("transacoes", conexao, if_exists="replace", index=False)

# Fecha a conexão com o banco
conexao.close()

print("Pipeline concluído! Dados salvos em pipeline.db, na tabela 'transacoes'.")
print(f"Total de linhas carregadas: {len(df)}")