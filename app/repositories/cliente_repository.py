from models.cliente import Cliente

class ClienteRepository:

    @staticmethod
    def create_cliente(nome, email):
        cliente = Cliente(nome=nome, email=email).save()
        return cliente

    @staticmethod
    def get_cliente_by_uid(uid):
        try:
            cliente = Cliente.nodes.get(uid=uid)
            return cliente
        except Cliente.DoesNotExist:
            return None

    @staticmethod
    def get_all_clientes():
        return Cliente.nodes.all()

    @staticmethod
    def delete_cliente(uid):
        cliente = ClienteRepository.get_cliente_by_uid(uid)
        if cliente:
            cliente.delete()
            return True
        return False
