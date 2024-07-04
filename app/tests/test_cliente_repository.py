import unittest
from models import Cliente
from repositories.cliente_repository import ClienteRepository

class ClienteRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.cliente_data = {
            "nome": "Teste",
            "email": "teste@example.com",
            "telefone": "(11) 1234-5678"
        }
        self.cliente = ClienteRepository.create_cliente(**self.cliente_data)

    def tearDown(self):
        ClienteRepository.delete_cliente(self.cliente.uid)

    def test_create_cliente(self):
        self.assertIsNotNone(self.cliente)
        self.assertEqual(self.cliente.nome, self.cliente_data["nome"])
        self.assertEqual(self.cliente.email, self.cliente_data["email"])
        self.assertEqual(self.cliente.telefone, self.cliente_data["telefone"])

    def test_delete_cliente(self):
        self.assertTrue(ClienteRepository.delete_cliente(self.cliente.uid))

    def test_get_all_clientes(self):
        clientes = ClienteRepository.get_all_clientes()
        self.assertGreater(len(clientes), 0)

    def test_get_cliente_by_uid(self):
        cliente = ClienteRepository.get_cliente_by_uid(self.cliente.uid)
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.uid, self.cliente.uid)

if __name__ == '__main__':
    unittest.main()
