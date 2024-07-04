import unittest
import json
from app import app

class HotelControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_hotel(self):
        response = self.app.post('/hoteis/create', json={
            'nome': 'Hotel Teste',
            'endereco_uid': 'uid-do-endereco'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_hotel(self):
        create_response = self.app.post('/hoteis/create', json={
            'nome': 'Hotel Teste',
            'endereco_uid': 'uid-do-endereco'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/hoteis/{uid}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_hotels(self):
        response = self.app.get('/hoteis/all')
        self.assertEqual(response.status_code, 200)

    def test_delete_hotel(self):
        create_response = self.app.post('/hoteis/create', json={
            'nome': 'Hotel Teste',
            'endereco_uid': 'uid-do-endereco'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/hoteis/delete/{uid}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
