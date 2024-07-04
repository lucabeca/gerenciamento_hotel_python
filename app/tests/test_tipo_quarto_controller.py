import unittest
import json
from app import app

class TipoQuartoControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_tipo_quarto(self):
        response = self.app.post('/tipos_quartos/', json={'descricao': 'Suite'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Suite', str(response.data))

    def test_get_tipo_quarto(self):
        create_response = self.app.post('/tipos_quartos/', json={'descricao': 'Suite'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/tipos_quartos/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Suite', str(response.data))

    def test_get_all_tipo_quartos(self):
        self.app.post('/tipos_quartos/', json={'descricao': 'Suite'})
        response = self.app.get('/tipos_quartos/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Suite', str(response.data))

    def test_delete_tipo_quarto(self):
        create_response = self.app.post('/tipos_quartos/', json={'descricao': 'Suite'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/tipos_quartos/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tipo de quarto deletado com sucesso', str(response.data))

if __name__ == '__main__':
    unittest.main()
