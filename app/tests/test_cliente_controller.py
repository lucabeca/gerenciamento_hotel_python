import unittest
import json
from app import app

class ClienteControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_cliente(self):
        response = self.app.post('/clientes/create', json={
            'nome': 'Cliente Teste',
            'telefone': '1234567890'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_cliente(self):
        create_response = self.app.post('/clientes/create', json={
            'nome': 'Cliente Teste',
            'telefone': '1234567890'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/clientes/{uid}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_clientes(self):
        response = self.app.get('/clientes/all')
        self.assertEqual(response.status_code, 200)

    def test_delete_cliente(self):
        create_response = self.app.post('/clientes/create', json={
            'nome': 'Cliente Teste',
            'telefone': '1234567890'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/clientes/delete/{uid}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
