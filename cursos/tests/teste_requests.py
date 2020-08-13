import requests

# GET AVALIAÇÔES
# avalicoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código do status HTTP
# print(avalicoes.status_code)

# Acessando os dados da resposta
# print(avalicoes.json())
# print(type(avalicoes.json()))

# Acessando a quantidade de resgistros
# print(avalicoes.json()['count'])

# acessando a próxima página de resultados
# print(avalicoes.json()['next'])

# acessando osresultados desta páginas
# print(avalicoes.json()['results'][-1])

# GET Avaliação
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1')
# print(avaliacao.json())

# GET CURSOS
# headers = {
#     'Authorization': 'Token 53c4b3d64d771025431b437772fde7f490f25d16'
# }
# cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
# print(cursos.json())
