"""
Este módulo lê um arquivo CSV e exibe suas primeiras linhas.
"""
import pandas as pd

tabela = pd.read_csv('ClientesBanco.csv', encoding='iso-8859-1')

"""Excluindo coluna CLIENTNUM"""
tabela = tabela.drop("CLIENTNUM", axis=1)

print(tabela.head())
