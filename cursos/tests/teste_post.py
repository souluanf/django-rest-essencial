import requests

headers = {
    'Authorization': 'Token 657bd365a6a46d9e01ee46b3b45521d4f2f47c4a'
}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Programação Rust 2",
    "url": "http://localhost:8000/progrust2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando código de status http
assert resultado.status_code == 201

# Testando se o titulo do curso criado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
