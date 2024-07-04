import unittest
from repositories.reserva_repository import ReservaRepository
from neomodel import db
from datetime import date

class ReservaRepositoryTest(unittest.TestCase):

    def setUp(self):
        db.cypher_query("MATCH (n) DETACH DELETE n")

    def test_create_reserva(self):
        reserva = ReservaRepository.create_reserva(data_inicio=date(2023, 1, 1), data_fim=date(2023, 1, 10), cliente="Cliente ABC", quarto="Quarto XYZ")
        self.assertIsNotNone(reserva)
        self.assertEqual(reserva.cliente, "Cliente ABC")
        self.assertEqual(reserva.quarto, "Quarto XYZ")

    def test_get_reserva_by_uid(self):
        reserva = ReservaRepository.create_reserva(data_inicio=date(2023, 1, 1), data_fim=date(2023, 1, 10), cliente="Cliente ABC", quarto="Quarto XYZ")
        retrieved_reserva = ReservaRepository.get_reserva_by_uid(reserva.uid)
        self.assertIsNotNone(retrieved_reserva)
        self.assertEqual(retrieved_reserva.uid, reserva.uid)

    def test_get_all_reservas(self):
        ReservaRepository.create_reserva(data_inicio=date(2023, 1, 1), data_fim=date(2023, 1, 10), cliente="Cliente ABC", quarto="Quarto XYZ")
        reservas = ReservaRepository.get_all_reservas()
        self.assertGreaterEqual(len(reservas), 1)

    def test_delete_reserva(self):
        reserva = ReservaRepository.create_reserva(data_inicio=date(2023, 1, 1), data_fim=date(2023, 1, 10), cliente="Cliente ABC", quarto="Quarto XYZ")
        self.assertTrue(ReservaRepository.delete_reserva(reserva.uid))
        self.assertIsNone(ReservaRepository.get_reserva_by_uid(reserva.uid))

if __name__ == '__main__':
    unittest.main()
