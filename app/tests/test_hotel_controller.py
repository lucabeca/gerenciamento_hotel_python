import unittest
import json
from app import app

class HotelControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_hotel(self):
        response = self.app.post('/hoteis/', json={'nome': 'Hotel ABC', 'endereco': 'Endereco XYZ'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Hotel ABC', str(response.data))

    def test_get_hotel(self):
        create_response = self.app.post('/hoteis/', json={'nome': 'Hotel ABC', 'endereco': 'Endereco XYZ'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/hoteis/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hotel ABC', str(response.data))

    def test_get_all_hotels(self):
        self.app.post('/hoteis/', json={'nome': 'Hotel ABC', 'endereco': 'Endereco XYZ'})
        response = self.app.get('/hoteis/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hotel ABC', str(response.data))

    def test_delete_hotel(self):
        create_response = self.app.post('/hoteis/', json={'nome': 'Hotel ABC', 'endereco': 'Endereco XYZ'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/hoteis/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hotel deletado com sucesso', str(response.data))

if __name__ == '__main__':
    unittest.main()
