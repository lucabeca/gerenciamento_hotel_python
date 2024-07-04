import unittest
import json
from app import app

class ReservaDetalheControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_reserva_detalhe(self):
        response = self.app.post('/reserva-detalhes/create', json={
            'reserva_uid': 'uid-da-reserva',
            'descricao': 'Detalhe da reserva'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_reserva_detalhe(self):
        create_response = self.app.post('/reserva-detalhes/create', json={
            'reserva_uid': 'uid-da-reserva',
            'descricao': 'Detalhe da reserva'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/reserva-detalhes/{uid}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_reserva_detalhes(self):
        response = self.app.get('/reserva-detalhes/all')
        self.assertEqual(response.status_code, 200)

    def test_delete_reserva_detalhe(self):
        create_response = self.app.post('/reserva-detalhes/create', json={
            'reserva_uid': 'uid-da-reserva',
            'descricao': 'Detalhe da reserva'
        })
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/reserva-detalhes/delete/{uid}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
