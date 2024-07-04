import unittest
from models import Endereco
from repositories.endereco_repository import EnderecoRepository

class EnderecoRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.endereco_data = {
            "rua": "Rua Teste",
            "numero": "123",
            "bairro": "Centro",
            "cidade": "Cidade Teste",
            "estado": "Estado Teste",
            "pais": "Brasil",
            "cep": "00000-000"
        }
        self.endereco = EnderecoRepository.create_endereco(**self.endereco_data)

    def tearDown(self):
        EnderecoRepository.delete_endereco(self.endereco.uid)

    def test_create_endereco(self):
        self.assertIsNotNone(self.endereco)
        self.assertEqual(self.endereco.rua, self.endereco_data["rua"])
        self.assertEqual(self.endereco.numero, self.endereco_data["numero"])

    def test_delete_endereco(self):
        self.assertTrue(EnderecoRepository.delete_endereco(self.endereco.uid))

    def test_get_all_enderecos(self):
        enderecos = EnderecoRepository.get_all_enderecos()
        self.assertGreater(len(enderecos), 0)

    def test_get_endereco_by_uid(self):
        endereco = EnderecoRepository.get_endereco_by_uid(self.endereco.uid)
        self.assertIsNotNone(endereco)
        self.assertEqual(endereco.uid, self.endereco.uid)

if __name__ == '__main__':
    unittest.main()
