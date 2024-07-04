import unittest
from repositories.reserva_detalhe_repository import ReservaDetalheRepository
from neomodel import db

class ReservaDetalheRepositoryTest(unittest.TestCase):

    def setUp(self):
        db.cypher_query("MATCH (n) DETACH DELETE n")

    def test_create_reserva_detalhe(self):
        reserva_detalhe = ReservaDetalheRepository.create_reserva_detalhe(reserva="Reserva ABC", detalhe="Detalhe XYZ")
        self.assertIsNotNone(reserva_detalhe)
        self.assertEqual(reserva_detalhe.reserva, "Reserva ABC")
        self.assertEqual(reserva_detalhe.detalhe, "Detalhe XYZ")

    def test_get_reserva_detalhe_by_uid(self):
        reserva_detalhe = ReservaDetalheRepository.create_reserva_detalhe(reserva="Reserva ABC", detalhe="Detalhe XYZ")
        retrieved_reserva_detalhe = ReservaDetalheRepository.get_reserva_detalhe_by_uid(reserva_detalhe.uid)
        self.assertIsNotNone(retrieved_reserva_detalhe)
        self.assertEqual(retrieved_reserva_detalhe.uid, reserva_detalhe.uid)

    def test_get_all_reserva_detalhes(self):
        ReservaDetalheRepository.create_reserva_detalhe(reserva="Reserva ABC", detalhe="Detalhe XYZ")
        reserva_detalhes = ReservaDetalheRepository.get_all_reserva_detalhes()
        self.assertGreaterEqual(len(reserva_detalhes), 1)

    def test_delete_reserva_detalhe(self):
        reserva_detalhe = ReservaDetalheRepository.create_reserva_detalhe(reserva="Reserva ABC", detalhe="Detalhe XYZ")
        self.assertTrue(ReservaDetalheRepository.delete_reserva_detalhe(reserva_detalhe.uid))
        self.assertIsNone(ReservaDetalheRepository.get_reserva_detalhe_by_uid(reserva_detalhe.uid))

if __name__ == '__main__':
    unittest.main()
