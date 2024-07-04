from neomodel import db
from models import Cliente

class ClienteRepository:

    @staticmethod
    def create_cliente(nome, email, telefone):
        cliente = Cliente(nome=nome, email=email, telefone=telefone)
        cliente.save()
        return cliente

    @staticmethod
    def delete_cliente(uid):
        cliente = Cliente.nodes.get_or_none(uid=uid)
        if cliente:
            cliente.delete()
            return True
        return False

    @staticmethod
    def get_all_clientes():
        return Cliente.nodes.all()

    @staticmethod
    def get_cliente_by_uid(uid):
        return Cliente.nodes.get_or_none(uid=uid)
