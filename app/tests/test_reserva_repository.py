import unittest
from models import Reserva
from repositories.reserva_repository import ReservaRepository

class ReservaRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.reserva_data = {
            "data_inicio": "2023-01-01",
            "data_fim": "2023-01-10",
            "forma_pagamento": "Cartão de Crédito"
        }
        self.reserva = ReservaRepository.create_reserva(**self.reserva_data)

    def tearDown(self):
        ReservaRepository.delete_reserva(self.reserva.uid)

    def test_create_reserva(self):
        self.assertIsNotNone(self.reserva)
        self.assertEqual(self.reserva.data_inicio, self.reserva_data["data_inicio"])
        self.assertEqual(self.reserva.data_fim, self.reserva_data["data_fim"])

    def test_delete_reserva(self):
        self.assertTrue(ReservaRepository.delete_reserva(self.reserva.uid))

    def test_get_all_reservas(self):
        reservas = ReservaRepository.get_all_reservas()
        self.assertGreater(len(reservas), 0)

    def test_get_reserva_by_uid(self):
        reserva = ReservaRepository.get_reserva_by_uid(self.reserva.uid)
        self.assertIsNotNone(reserva)
        self.assertEqual(reserva.uid, self.reserva.uid)

if __name__ == '__main__':
    unittest.main()
