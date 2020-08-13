import requests

headers = {
    'Authorization': 'Token 657bd365a6a46d9e01ee46b3b45521d4f2f47c4a'
}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

resultado = requests.delete(url=f'{url_base_cursos}9/', headers=headers)

# Testando código status HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteudo retornado é 0
assert len(resultado.text) == 0
