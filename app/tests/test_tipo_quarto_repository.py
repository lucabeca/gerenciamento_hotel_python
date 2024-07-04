import unittest
from repositories.tipo_quarto_repository import TipoQuartoRepository
from neomodel import db

class TipoQuartoRepositoryTest(unittest.TestCase):

    def setUp(self):
        db.cypher_query("MATCH (n) DETACH DELETE n")

    def test_create_tipo_quarto(self):
        tipo_quarto = TipoQuartoRepository.create_tipo_quarto(descricao="Suite")
        self.assertIsNotNone(tipo_quarto)
        self.assertEqual(tipo_quarto.descricao, "Suite")

    def test_get_tipo_quarto_by_uid(self):
        tipo_quarto = TipoQuartoRepository.create_tipo_quarto(descricao="Suite")
        retrieved_tipo_quarto = TipoQuartoRepository.get_tipo_quarto_by_uid(tipo_quarto.uid)
        self.assertIsNotNone(retrieved_tipo_quarto)
        self.assertEqual(retrieved_tipo_quarto.uid, tipo_quarto.uid)

    def test_get_all_tipo_quartos(self):
        TipoQuartoRepository.create_tipo_quarto(descricao="Suite")
        tipo_quartos = TipoQuartoRepository.get_all_tipo_quartos()
        self.assertGreaterEqual(len(tipo_quartos), 1)

    def test_delete_tipo_quarto(self):
        tipo_quarto = TipoQuartoRepository.create_tipo_quarto(descricao="Suite")
        self.assertTrue(TipoQuartoRepository.delete_tipo_quarto(tipo_quarto.uid))
        self.assertIsNone(TipoQuartoRepository.get_tipo_quarto_by_uid(tipo_quarto.uid))

if __name__ == '__main__':
    unittest.main()
