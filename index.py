"""
Este módulo lê um arquivo CSV e exibe suas primeiras linhas.
"""
import pandas as pd

# Exibir todas as colunas e linhas
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

tabela = pd.read_csv('ClientesBanco.csv', encoding='iso-8859-1')

# Excluindo coluna desnecessárias - CLIENTNUM
tabela = tabela.drop("CLIENTNUM", axis=1)
# print(tabela.dtypes)

# Remover o(s) registro(s) com ausência de valor
tabela = tabela.dropna()
tabela.info()
# print(tabela.head())

print(tabela.describe().round(1))

# Exibir todas as colunas e linhas

# for coluna in tabela.columns:
#     if tabela[coluna].dtype == 'object':
