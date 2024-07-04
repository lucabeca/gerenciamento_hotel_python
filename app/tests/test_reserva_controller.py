import unittest
import json
from datetime import date
from app import app

class ReservaControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_reserva(self):
        response = self.app.post('/reservas/create', json={
            'cliente_uid': 'uid-do-cliente',
            'quarto_uid': 'uid-do-quarto',
            'data_inicio': '2023-01-01',
            'data_fim': '2023-01-07'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_reserva(self):
        create_response = self.app.post('/reservas/create', json={
            'cliente_uid': 'uid-do-cliente',
            'quarto_uid': 'uid-do-quarto',
            'data_inicio': '2023-01-01',
            'data_fim': '2023-01-07'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/reservas/{uid}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_reservas(self):
        response = self.app.get('/reservas/all')
        self.assertEqual(response.status_code, 200)

    def test_delete_reserva(self):
        create_response = self.app.post('/reservas/create', json={
            'cliente_uid': 'uid-do-cliente',
            'quarto_uid': 'uid-do-quarto',
            'data_inicio': '2023-01-01',
            'data_fim': '2023-01-07'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/reservas/delete/{uid}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
