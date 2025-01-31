import pandas as pd
from apyori import apriori

dados = pd.read_csv('transacoes.txt', header = None)
transacoes = []
for i in range(0,6):
    transacoes.append([str(dados.values[i,j]) for j in range(0,3)]) # deixando os dados no formato lista encadeada(necessario)
    
regras = apriori(transacoes, min_support = 0.5, min_confidence = 0.5)

resultados = list(regras) # mostra o resultado das regras

resultados2 = [list(x) for x in resultados]

resultados3 = []
for j in range(0,7):
    resultados3.append([list(x) for x in resultados2[j][2]])