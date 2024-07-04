import unittest
from repositories.quarto_repository import QuartoRepository
from neomodel import db

class QuartoRepositoryTest(unittest.TestCase):

    def setUp(self):
        db.cypher_query("MATCH (n) DETACH DELETE n")

    def test_create_quarto(self):
        quarto = QuartoRepository.create_quarto(numero="101", tipo="Suite", capacidade=2, hotel="Hotel ABC")
        self.assertIsNotNone(quarto)
        self.assertEqual(quarto.numero, "101")
        self.assertEqual(quarto.tipo, "Suite")

    def test_get_quarto_by_uid(self):
        quarto = QuartoRepository.create_quarto(numero="101", tipo="Suite", capacidade=2, hotel="Hotel ABC")
        retrieved_quarto = QuartoRepository.get_quarto_by_uid(quarto.uid)
        self.assertIsNotNone(retrieved_quarto)
        self.assertEqual(retrieved_quarto.uid, quarto.uid)

    def test_get_all_quartos(self):
        QuartoRepository.create_quarto(numero="101", tipo="Suite", capacidade=2, hotel="Hotel ABC")
        quartos = QuartoRepository.get_all_quartos()
        self.assertGreaterEqual(len(quartos), 1)

    def test_delete_quarto(self):
        quarto = QuartoRepository.create_quarto(numero="101", tipo="Suite", capacidade=2, hotel="Hotel ABC")
        self.assertTrue(QuartoRepository.delete_quarto(quarto.uid))
        self.assertIsNone(QuartoRepository.get_quarto_by_uid(quarto.uid))

if __name__ == '__main__':
    unittest.main()
