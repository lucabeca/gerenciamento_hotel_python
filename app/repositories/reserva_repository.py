from neomodel import db
from models import Reserva

class ReservaRepository:

    @staticmethod
    def create_reserva(data_inicio, data_fim, forma_pagamento):
        reserva = Reserva(data_inicio=data_inicio, data_fim=data_fim, forma_pagamento=forma_pagamento)
        reserva.save()
        return reserva

    @staticmethod
    def delete_reserva(uid):
        reserva = Reserva.nodes.get_or_none(uid=uid)
        if reserva:
            reserva.delete()
            return True
        return False

    @staticmethod
    def get_all_reservas():
        return Reserva.from models import Reserva
from datetime import datetime

class ReservaRepository:
    @staticmethod
    def create_reserva(cliente_uid, quarto_uid, data_inicio, data_fim):
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
        reserva = Reserva(cliente_uid=cliente_uid, quarto_uid=quarto_uid, data_inicio=data_inicio, data_fim=data_fim)
        reserva.save()
        return reserva

    @staticmethod
    def get_reserva_by_uid(uid):
        return Reserva.nodes.get(uid=uid)

    @staticmethod
    def get_all_reservas():
        return Reserva.nodes.all()

    @staticmethod
    def delete_reserva(uid):
        reserva = Reserva.nodes.get(uid=uid)
        reserva.delete()
nodes.all()

    @staticmethod
    def get_reserva_by_uid(uid):
        return Reserva.nodes.get_or_none(uid=uid)
