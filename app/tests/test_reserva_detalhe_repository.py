import unittest
from models import ReservaDetalhe
from repositories.reserva_detalhe_repository import ReservaDetalheRepository

class ReservaDetalheRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.reserva_detalhe_data = {
            "reserva_uid": "some-reserva-uid",
            "quarto_uid": "some-quarto-uid",
            "cliente_uid": "some-cliente-uid"
        }
        self.reserva_detalhe = ReservaDetalheRepository.create_reserva_detalhe(**self.reserva_detalhe_data)

    def tearDown(self):
        ReservaDetalheRepository.delete_reserva_detalhe(self.reserva_detalhe.uid)

    def test_create_reserva_detalhe(self):
        self.assertIsNotNone(self.reserva_detalhe)
        self.assertEqual(self.reserva_detalhe.reserva_uid, self.reserva_detalhe_data["reserva_uid"])
        self.assertEqual(self.reserva_detalhe.quarto_uid, self.reserva_detalhe_data["quarto_uid"])

    def test_delete_reserva_detalhe(self):
        self.assertTrue(ReservaDetalheRepository.delete_reserva_detalhe(self.reserva_detalhe.uid))

    def test_get_all_reserva_detalhes(self):
        reserva_detalhes = ReservaDetalheRepository.get_all_reserva_detalhes()
        self.assertGreater(len(reserva_detalhes), 0)

    def test_get_reserva_detalhe_by_uid(self):
        reserva_detalhe = ReservaDetalheRepository.get_reserva_detalhe_by_uid(self.reserva_detalhe.uid)
        self.assertIsNotNone(reserva_detalhe)
        self.assertEqual(reserva_detalhe.uid, self.reserva_detalhe.uid)

if __name__ == '__main__':
    unittest.main()
