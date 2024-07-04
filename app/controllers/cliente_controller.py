class ClienteRepository:
    @staticmethod
    def delete_cliente(uid):
        try:
            cliente = Cliente.nodes.get(uid=uid)
            cliente.delete()
            return True
        except Cliente.DoesNotExist:
            return False

    @staticmethod
    def get_cliente_by_uid(uid):
        try:
            return Cliente.nodes.get(uid=uid)
        except Cliente.DoesNotExist:
            return None

    @staticmethod
    def get_all_clientes():
        return Cliente.nodes.all()
