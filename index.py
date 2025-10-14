"""
Este módulo lê um arquivo CSV para análise.
"""
import pandas as pd
import plotly.express as px


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

# Exibição de um resumo estatístico das colunas numéricas da base de dados
print(tabela.describe().round(1))

# Avaliação entre Clientes X Cancelados

qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
print(qtde_categoria_perc)

# Análise das várias formas do motivo de cancelamento

# - Olhar a comparação entre Clientes e Cancelados em cada uma das colunas
# procurando novos insights

for coluna in tabela:
    histograma = px.histogram(tabela, x=coluna, color="Categoria")
    histograma.show()

# Informações retiradas da análise

# Me parece que quanto mais produtos contratatos
# um cliente tem, menor a chance dele cancelar

# Quanto mais transações e quanto maior o valor
# de transação, menor as chances de cancelar

# Quanto maior a quantidade de contatos que a pessoa
# teve que fazer, maior as chances de cancelar
