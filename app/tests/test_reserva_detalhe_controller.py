import unittest
import json
from app import app

class ReservaDetalheControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_reserva_detalhe(self):
        response = self.app.post('/reservas_detalhes/', json={'reserva': 'Reserva ABC', 'detalhe': 'Detalhe XYZ'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Detalhe XYZ', str(response.data))

    def test_get_reserva_detalhe(self):
        create_response = self.app.post('/reservas_detalhes/', json={'reserva': 'Reserva ABC', 'detalhe': 'Detalhe XYZ'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/reservas_detalhes/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Detalhe XYZ', str(response.data))

    def test_get_all_reserva_detalhes(self):
        self.app.post('/reservas_detalhes/', json={'reserva': 'Reserva ABC', 'detalhe': 'Detalhe XYZ'})
        response = self.app.get('/reservas_detalhes/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Detalhe XYZ', str(response.data))

    def test_delete_reserva_detalhe(self):
        create_response = self.app.post('/reservas_detalhes/', json={'reserva': 'Reserva ABC', 'detalhe': 'Detalhe XYZ'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/reservas_detalhes/{uid}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Detalhe da reserva deletado com sucesso', str(response.data))

if __name__ == '__main__':
    unittest.main()
