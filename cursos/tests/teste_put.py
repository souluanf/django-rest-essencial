import requests

headers = {
    'Authorization': 'Token 657bd365a6a46d9e01ee46b3b45521d4f2f47c4a'
}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

curso_atualizado = {
    "titulo": "Novo Curso de Programação Rust",
    "url": "http://localhost:8000/novoprogrust"
}

# Buscando o curso com ID 7
# curso = requests.get(url=f'{url_base_cursos}7/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}7/', headers=headers, data=curso_atualizado)

# Testando código status HTTP
assert resultado.status_code == 200

# Testando titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']
