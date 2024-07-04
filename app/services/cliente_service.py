from repositories.cliente_repository import ClienteRepository

class ClienteService:

    @staticmethod
    def create_cliente(nome, email):
        return ClienteRepository.create_cliente(nome, email)

    @staticmethod
    def get_cliente_by_uid(uid):
        return ClienteRepository.get_cliente_by_uid(uid)

    @staticmethod
    def get_all_clientes():
        return ClienteRepository.get_all_clientes()

    @staticmethod
    def delete_cliente(uid):
        return ClienteRepository.delete_cliente(uid)
