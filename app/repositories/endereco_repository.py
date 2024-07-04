from neomodel import db
from models import Endereco

class EnderecoRepository:

    @staticmethod
    def create_endereco(rua, numero, bairro, cidade, estado, pais, cep):
        endereco = Endereco(rua=rua, numero=numero, bairro=bairro, cidade=cidade, estado=estado, pais=pais, cep=cep)
        endereco.save()
        return endereco

    @staticmethod
    def delete_endereco(uid):
        endereco = Endereco.nodes.get_or_none(uid=uid)
        if endereco:
            endereco.delete()
            return True
        return False

    @staticmethod
    def get_all_enderecos():
        return Endereco.nodes.all()

    @staticmethod
    def get_endereco_by_uid(uid):
        return Endereco.nodes.get_or_none(uid=uid)
