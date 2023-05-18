# Passo 1: Pegar/Importar a base de dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")
tabela = tabela.drop("Unnamed: 8", axis=1)
# Passo 2: Visualizar a Base de Dados

print(tabela)
# Passo 3: Tratamento de dados
tabela["Salario Anual (R$)"] = pd.to_numeric(tabela["Salario Anual (R$)"], errors="coerce")

tabela = tabela.dropna()
print(tabela.info())
# Passo 4: Analise Inicial = entender como estão as notas dos clientes
print(tabela.describe())

# Passo 5: Analise Completa = Traçar o perfil ideal de clientes e entender como cada características do cliente
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    grafico.show()