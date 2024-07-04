import unittest
from models import TipoQuarto
from repositories.tipo_quarto_repository import TipoQuartoRepository

class TipoQuartoRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.tipo_quarto_data = {
            "tipo": "Standard",
            "capacidade": 2,
            "descricao": "Quarto simples com cama de casal"
        }
        self.tipo_quarto = TipoQuartoRepository.create_tipo_quarto(**self.tipo_quarto_data)

    def tearDown(self):
        TipoQuartoRepository.delete_tipo_quarto(self.tipo_quarto.uid)

    def test_create_tipo_quarto(self):
        self.assertIsNotNone(self.tipo_quarto)
        self.assertEqual(self.tipo_quarto.tipo, self.tipo_quarto_data["tipo"])
        self.assertEqual(self.tipo_quarto.capacidade, self.tipo_quarto_data["capacidade"])

    def test_delete_tipo_quarto(self):
        self.assertTrue(TipoQuartoRepository.delete_tipo_quarto(self.tipo_quarto.uid))

    def test_get_all_tipo_quartos(self):
        tipos_quartos = TipoQuartoRepository.get_all_tipo_quartos()
        self.assertGreater(len(tipos_quartos), 0)

    def test_get_tipo_quarto_by_uid(self):
        tipo_quarto = TipoQuartoRepository.get_tipo_quarto_by_uid(self.tipo_quarto.uid)
        self.assertIsNotNone(tipo_quarto)
        self.assertEqual(tipo_quarto.uid, self.tipo_quarto.uid)

if __name__ == '__main__':
    unittest.main()
