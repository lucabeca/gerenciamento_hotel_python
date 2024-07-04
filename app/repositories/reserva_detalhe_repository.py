from models.reserva_detalhe import ReservaDetalhe

class ReservaDetalheRepository:

    @staticmethod
    def create_reserva_detalhe(reserva, detalhe):
        reserva_detalhe = ReservaDetalhe(reserva=reserva, detalhe=detalhe).save()
        return reserva_detalhe

    @staticmethod
    def get_reserva_detalhe_by_uid(uid):
        try:
            reserva_detalhe = ReservaDetalhe.nodes.get(uid=uid)
            return reserva_detalhe
        except ReservaDetalhe.DoesNotExist:
            return None

    @staticmethod
    def get_all_reserva_detalhes():
        return ReservaDetalhe.nodes.all()

    @staticmethod
    def delete_reserva_detalhe(uid):
        reserva_detalhe = ReservaDetalheRepository.get_reserva_detalhe_by_uid(uid)
        if reserva_detalhe:
            reserva_detalhe.delete()
            return True
        return False
