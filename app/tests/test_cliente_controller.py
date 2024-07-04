import unittest
import json
from app import app

class ClienteControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_cliente(self):
        response = self.app.post('/clientes/', json={'nome': 'John Doe', 'email': 'john.doe@example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('John Doe', str(response.data))

    def test_get_cliente(self):
        create_response = self.app.post('/clientes/', json={'nome': 'John Doe', 'email': 'john.doe@example.com'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/clientes/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', str(response.data))

    def test_get_all_clientes(self):
        self.app.post('/clientes/', json={'nome': 'John Doe', 'email': 'john.doe@example.com'})
        response = self.app.get('/clientes/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', str(response.data))

    def test_delete_cliente(self):
        create_response = self.app.post('/clientes/', json={'nome': 'John Doe', 'email': 'john.doe@example.com'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/clientes/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Cliente deletado com sucesso', str(response.data))

if __name__ == '__main__':
    unittest.main()
