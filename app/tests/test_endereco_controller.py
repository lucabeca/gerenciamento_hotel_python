import unittest
import json
from app import app

class EnderecoControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_endereco(self):
        response = self.app.post('/enderecos/create', json={
            'rua': 'Rua Teste',
            'numero': '123',
            'bairro': 'Bairro Teste',
            'cidade': 'Cidade Teste',
            'estado': 'Estado Teste',
            'pais': 'Pais Teste',
            'cep': '12345-678'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_endereco(self):
        create_response = self.app.post('/enderecos/create', json={
            'rua': 'Rua Teste',
            'numero': '123',
            'bairro': 'Bairro Teste',
            'cidade': 'Cidade Teste',
            'estado': 'Estado Teste',
            'pais': 'Pais Teste',
            'cep': '12345-678'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/enderecos/{uid}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_enderecos(self):
        response = self.app.get('/enderecos/all')
        self.assertEqual(response.status_code, 200)

    def test_delete_endereco(self):
        create_response = self.app.post('/enderecos/create', json={
            'rua': 'Rua Teste',
            'numero': '123',
            'bairro': 'Bairro Teste',
            'cidade': 'Cidade Teste',
            'estado': 'Estado Teste',
            'pais': 'Pais Teste',
            'cep': '12345-678'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/enderecos/delete/{uid}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
