import requests


class TestCursos:
    headers = {'Authorization': 'Token 657bd365a6a46d9e01ee46b3b45521d4f2f47c4a'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}3/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            'titulo': 'Programação com Ruby',
            'url': 'http://localhost:8000/ruby'
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Programação Rust",
            "url": "http://localhost:8000/prog-rust"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Programação Rust 2",
            "url": "http://localhost:8000/prog-rust2"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}3/', headers=self.headers, data=atualizado)
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resultado = requests.delete(url=f'{self.url_base_cursos}11/', headers=self.headers)

        assert resultado.status_code == 204 and len(resultado.text) == 0
