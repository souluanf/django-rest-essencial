import requests

headers = {
    'Authorization': 'Token 657bd365a6a46d9e01ee46b3b45521d4f2f47c4a'
}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
print(resultado.json())

# Testando o endpoint está corrreto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 4


# Testando se o titulo do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Curso completo Java'
