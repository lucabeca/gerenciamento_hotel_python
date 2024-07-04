import unittest
import json
from app import app

class TipoQuartoControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_tipo_quarto(self):
        response = self.app.post('/tipo-quartos/create', json={
            'descricao': 'Tipo de Quarto Teste'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_tipo_quarto(self):
        create_response = self.app.post('/tipo-quartos/create', json={
            'descricao': 'Tipo de Quarto Teste'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/tipo-quartos/{uid}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_tipo_quartos(self):
        response = self.app.get('/tipo-quartos/all')
        self.assertEqual(response.status_code, 200)

    def test_delete_tipo_quarto(self):
        create_response = self.app.post('/tipo-quartos/create', json={
            'descricao': 'Tipo de Quarto Teste'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/tipo-quartos/delete/{uid}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
