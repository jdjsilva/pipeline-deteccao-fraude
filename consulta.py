import sqlite3
import pandas as pd

# Conecta ao banco
conexao = sqlite3.connect("pipeline.db")

# Faz uma consulta SQL simples: pega as 10 primeiras linhas
resultado = pd.read_sql("SELECT * FROM transacoes LIMIT 10", conexao)
print(resultado)

# Bônus: conta quantas transações foram sinalizadas como suspeitas
total_suspeitas = pd.read_sql(
    "SELECT COUNT(*) as total FROM transacoes WHERE flag_suspeita = 1", 
    conexao
)
print("\nTotal de transações suspeitas:")
print(total_suspeitas)

conexao.close()