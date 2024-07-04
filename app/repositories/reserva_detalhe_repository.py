from neomodel import db
from models import ReservaDetalhe

class ReservaDetalheRepository:

    @staticmethod
    def create_reserva_detalhe(reserva_uid, quarto_uid, cliente_uid):
        reserva_detalhe = ReservaDetalhe(reserva_uid=reserva_uid, quarto_uid=quarto_uid, cliente_uid=cliente_uid)
        reserva_detalhe.save()
        return reserva_detalhe

    @staticmethod
    def delete_reserva_detalhe(uid):
        reserva_detalhe = ReservaDetalhe.nodes.get_or_none(uid=uid)
        if reserva_detalhe:
            reserva_detalhe.delete()
            return True
        return False

    @staticmethod
    def get_all_reserva_detalhes():
        return ReservaDetalhe.nodes.all()

    @staticmethod
    def get_reserva_detalhe_by_uid(uid):
        return ReservaDetalhe.nodes.get_or_none(uid=uid)
