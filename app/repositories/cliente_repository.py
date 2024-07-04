from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class Cliente(StructuredNode):
    uid = UniqueIdProperty()
    nome = StringProperty(required=True)
    email = StringProperty()

class ClienteRepository:

    @staticmethod
    def create_cliente(nome, email):
        cliente = Cliente(nome=nome, email=email)
        cliente.save()

    @staticmethod
    def get_all_clientes():
        return Cliente.nodes.all()

    @staticmethod
    def get_cliente_by_uid(uid):
        try:
            return Cliente.nodes.get(uid=uid)
        except Cliente.DoesNotExist:
            return None

    @staticmethod
    def delete_cliente(uid):
        cliente = ClienteRepository.get_cliente_by_uid(uid)
        if cliente:
            cliente.delete()
            return True
        return False
