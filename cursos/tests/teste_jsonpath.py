import requests
import jsonpath

# GET AVALIAÇÔES
avalicoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avalicoes.json(), 'results')
# print(resultados)


# primeira = jsonpath.jsonpath(avalicoes.json(), 'results[0]')
# print(primeira)

# nome = jsonpath.jsonpath(avalicoes.json(), 'results[0].nome')[0]
# print(nome)

# nota_data = jsonpath.jsonpath(avalicoes.json(), 'results[0].avaliacao')[0]
# print(nota_data)

# Todos os nomes das pessoas que avaliaram o curso
nomes = jsonpath.jsonpath(avalicoes.json(),'results[*].nome')
print(nomes)
