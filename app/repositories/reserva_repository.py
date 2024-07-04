from models.reserva import Reserva

class ReservaRepository:

    @staticmethod
    def create_reserva(data_inicio, data_fim, cliente, quarto):
        reserva = Reserva(data_inicio=data_inicio, data_fim=data_fim, cliente=cliente, quarto=quarto).save()
        return reserva

    @staticmethod
    def get_reserva_by_uid(uid):
        try:
            reserva = Reserva.nodes.get(uid=uid)
            return reserva
        except Reserva.DoesNotExist:
            return None

    @staticmethod
    def get_all_reservas():
        return Reserva.nodes.all()

    @staticmethod
    def delete_reserva(uid):
        reserva = ReservaRepository.get_reserva_by_uid(uid)
        if reserva:
            reserva.delete()
            return True
        return False
