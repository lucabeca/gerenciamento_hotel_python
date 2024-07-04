import unittest
from repositories.cliente_repository import ClienteRepository
from neomodel import db

class ClienteRepositoryTest(unittest.TestCase):

    def setUp(self):
        db.cypher_query("MATCH (n) DETACH DELETE n")

    def test_create_cliente(self):
        cliente = ClienteRepository.create_cliente(nome="John Doe", email="john.doe@example.com")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nome, "John Doe")
        self.assertEqual(cliente.email, "john.doe@example.com")

    def test_get_cliente_by_uid(self):
        cliente = ClienteRepository.create_cliente(nome="John Doe", email="john.doe@example.com")
        retrieved_cliente = ClienteRepository.get_cliente_by_uid(cliente.uid)
        self.assertIsNotNone(retrieved_cliente)
        self.assertEqual(retrieved_cliente.uid, cliente.uid)

    def test_get_all_clientes(self):
        ClienteRepository.create_cliente(nome="John Doe", email="john.doe@example.com")
        clientes = ClienteRepository.get_all_clientes()
        self.assertGreaterEqual(len(clientes), 1)

    def test_delete_cliente(self):
        cliente = ClienteRepository.create_cliente(nome="John Doe", email="john.doe@example.com")
        self.assertTrue(ClienteRepository.delete_cliente(cliente.uid))
        self.assertIsNone(ClienteRepository.get_cliente_by_uid(cliente.uid))

if __name__ == '__main__':
    unittest.main()
