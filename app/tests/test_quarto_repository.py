import unittest
from models import Quarto
from repositories.quarto_repository import QuartoRepository

class QuartoRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.quarto_data = {
            "numero": "101",
            "disponibilidade": True,
            "preco": 100.0
        }
        self.quarto = QuartoRepository.create_quarto(**self.quarto_data)

    def tearDown(self):
        QuartoRepository.delete_quarto(self.quarto.uid)

    def test_create_quarto(self):
        self.assertIsNotNone(self.quarto)
        self.assertEqual(self.quarto.numero, self.quarto_data["numero"])
        self.assertEqual(self.quarto.disponibilidade, self.quarto_data["disponibilidade"])

    def test_delete_quarto(self):
        self.assertTrue(QuartoRepository.delete_quarto(self.quarto.uid))

    def test_get_all_quartos(self):
        quartos = QuartoRepository.get_all_quartos()
        self.assertGreater(len(quartos), 0)

    def test_get_quarto_by_uid(self):
        quarto = QuartoRepository.get_quarto_by_uid(self.quarto.uid)
        self.assertIsNotNone(quarto)
        self.assertEqual(quarto.uid, self.quarto.uid)

if __name__ == '__main__':
    unittest.main()
