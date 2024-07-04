import unittest
import json
from app import app

class ReservaControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_reserva(self):
        response = self.app.post('/reservas/', json={'data_inicio': '2023-01-01', 'data_fim': '2023-01-10', 'cliente': 'Cliente ABC', 'quarto': 'Quarto XYZ'})
        response_data = response.get_data(as_text=True)
        print(f"Response data (create_reserva): {response_data}")
        self.assertEqual(response.status_code, 201)
        self.assertIn('Sun, 01 Jan 2023 00:00:00 GMT', response_data)

    def test_get_reserva(self):
        create_response = self.app.post('/reservas/', json={'data_inicio': '2023-01-01', 'data_fim': '2023-01-10', 'cliente': 'Cliente ABC', 'quarto': 'Quarto XYZ'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.get(f'/reservas/{uid}')
        response_data = response.get_data(as_text=True)
        print(f"Response data (get_reserva): {response_data}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sun, 01 Jan 2023 00:00:00 GMT', response_data)

    def test_get_all_reservas(self):
        self.app.post('/reservas/', json={'data_inicio': '2023-01-01', 'data_fim': '2023-01-10', 'cliente': 'Cliente ABC', 'quarto': 'Quarto XYZ'})
        response = self.app.get('/reservas/')
        response_data = response.get_data(as_text=True)
        print(f"Response data (get_all_reservas): {response_data}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sun, 01 Jan 2023 00:00:00 GMT', response_data)

    def test_delete_reserva(self):
        create_response = self.app.post('/reservas/', json={'data_inicio': '2023-01-01', 'data_fim': '2023-01-10', 'cliente': 'Cliente ABC', 'quarto': 'Quarto XYZ'})
        uid = json.loads(create_response.data)['uid']
        response = self.app.delete(f'/reservas/{uid}')
        response_data = response.get_data(as_text=True)
        print(f"Response data (delete_reserva): {response_data}")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Reserva deletada com sucesso', response_data)

if __name__ == '__main__':
    unittest.main()
