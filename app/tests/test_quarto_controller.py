import unittest
import json
from app import app

class QuartoControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_quarto(self):
        response = self.app.post('/quartos/', json={'numero': '101', 'tipo': 'Suite', 'capacidade': 2, 'hotel': 'Hotel ABC'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('101', str(response.data))

    def test_get_quarto(self):
        create_response = self.app.post('/quartos/', json={'numero': '101', 'tipo': 'Suite', 'capacidade': 2, 'hotel': 'Hotel ABC'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/quartos/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('101', str(response.data))

    def test_get_all_quartos(self):
        self.app.post('/quartos/', json={'numero': '101', 'tipo': 'Suite', 'capacidade': 2, 'hotel': 'Hotel ABC'})
        response = self.app.get('/quartos/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('101', str(response.data))

    def test_delete_quarto(self):
        create_response = self.app.post('/quartos/', json={'numero': '101', 'tipo': 'Suite', 'capacidade': 2, 'hotel': 'Hotel ABC'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/quartos/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Quarto deletado com sucesso', str(response.data))

if __name__ == '__main__':
    unittest.main()
