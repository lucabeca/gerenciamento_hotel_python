import unittest
import json
from app import app

class QuartoControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_quarto(self):
        response = self.app.post('/quartos/create', json={
            'numero': 101,
            'tipo_uid': 'uid-do-tipo'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_quarto(self):
        create_response = self.app.post('/quartos/create', json={
            'numero': 101,
            'tipo_uid': 'uid-do-tipo'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/quartos/{uid}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_quartos(self):
        response = self.app.get('/quartos/all')
        self.assertEqual(response.status_code, 200)

    def test_delete_quarto(self):
        create_response = self.app.post('/quartos/create', json={
            'numero': 101,
            'tipo_uid': 'uid-do-tipo'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/quartos/delete/{uid}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
