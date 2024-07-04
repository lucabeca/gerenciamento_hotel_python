import unittest
import json
from app import app

class EnderecoControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_endereco(self):
        response = self.app.post('/enderecos/', json={'rua': 'Rua ABC', 'cidade': 'Cidade XYZ', 'estado': 'Estado QW', 'cep': '12345-678'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Rua ABC', str(response.data))

    def test_get_endereco(self):
        create_response = self.app.post('/enderecos/', json={'rua': 'Rua ABC', 'cidade': 'Cidade XYZ', 'estado': 'Estado QW', 'cep': '12345-678'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/enderecos/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Rua ABC', str(response.data))

    def test_get_all_enderecos(self):
        self.app.post('/enderecos/', json={'rua': 'Rua ABC', 'cidade': 'Cidade XYZ', 'estado': 'Estado QW', 'cep': '12345-678'})
        response = self.app.get('/enderecos/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Rua ABC', str(response.data))

    def test_delete_endereco(self):
        create_response = self.app.post('/enderecos/', json={'rua': 'Rua ABC', 'cidade': 'Cidade XYZ', 'estado': 'Estado QW', 'cep': '12345-678'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/enderecos/{uid}')
        print(f"Response data: {response.get_data(as_text=True)}")  # Adicionar log
        self.assertEqual(response.status_code, 200)
        self.assertIn('Endereço deletado com sucesso', response.get_data(as_text=True).replace("\\u00e7", "ç"))

if __name__ == '__main__':
    unittest.main()
