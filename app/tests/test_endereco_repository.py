import unittest
from repositories.endereco_repository import EnderecoRepository
from neomodel import db

class EnderecoRepositoryTest(unittest.TestCase):

    def setUp(self):
        db.cypher_query("MATCH (n) DETACH DELETE n")

    def test_create_endereco(self):
        endereco = EnderecoRepository.create_endereco(rua="Rua ABC", cidade="Cidade XYZ", estado="Estado QW", cep="12345-678")
        self.assertIsNotNone(endereco)
        self.assertEqual(endereco.rua, "Rua ABC")
        self.assertEqual(endereco.cidade, "Cidade XYZ")

    def test_get_endereco_by_uid(self):
        endereco = EnderecoRepository.create_endereco(rua="Rua ABC", cidade="Cidade XYZ", estado="Estado QW", cep="12345-678")
        retrieved_endereco = EnderecoRepository.get_endereco_by_uid(endereco.uid)
        self.assertIsNotNone(retrieved_endereco)
        self.assertEqual(retrieved_endereco.uid, endereco.uid)

    def test_get_all_enderecos(self):
        EnderecoRepository.create_endereco(rua="Rua ABC", cidade="Cidade XYZ", estado="Estado QW", cep="12345-678")
        enderecos = EnderecoRepository.get_all_enderecos()
        self.assertGreaterEqual(len(enderecos), 1)

    def test_delete_endereco(self):
        endereco = EnderecoRepository.create_endereco(rua="Rua ABC", cidade="Cidade XYZ", estado="Estado QW", cep="12345-678")
        self.assertTrue(EnderecoRepository.delete_endereco(endereco.uid))
        self.assertIsNone(EnderecoRepository.get_endereco_by_uid(endereco.uid))

if __name__ == '__main__':
    unittest.main()
