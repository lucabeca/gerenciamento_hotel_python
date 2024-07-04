from neomodel import db
from models import TipoQuarto

class TipoQuartoRepository:

    @staticmethod
    def create_tipo_quarto(tipo, capacidade, descricao):
        tipo_quarto = TipoQuarto(tipo=tipo, capacidade=capacidade, descricao=descricao)
        tipo_quarto.save()
        return tipo_quarto

    @staticmethod
    def delete_tipo_quarto(uid):
        tipo_quarto = TipoQuarto.nodes.get_or_none(uid=uid)
        if tipo_quarto:
            tipo_quarto.delete()
            return True
        return False

    @staticmethod
    def get_all_tipo_quartos():
        return TipoQuarto.nodes.all()

    @staticmethod
    def get_tipo_quarto_by_uid(uid):
        return TipoQuarto.nodes.get_or_none(uid=uid)
