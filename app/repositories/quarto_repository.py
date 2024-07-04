from neomodel import db
from models import Quarto

class QuartoRepository:

    @staticmethod
    def create_quarto(numero, disponibilidade, preco):
        quarto = Quarto(numero=numero, disponibilidade=disponibilidade, preco=preco)
        quarto.save()
        return quarto

    @staticmethod
    def delete_quarto(uid):
        quarto = Quarto.nodes.get_or_none(uid=uid)
        if quarto:
            quarto.delete()
            return True
        return False

    @staticmethod
    def get_all_quartos():
        return Quarto.nodes.all()

    @staticmethod
    def get_quarto_by_uid(uid):
        return Quarto.nodes.get_or_none(uid=uid)
