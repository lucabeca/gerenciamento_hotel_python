from repositories.reserva_detalhe_repository import ReservaDetalheRepository

class ReservaDetalheService:

    @staticmethod
    def create_reserva_detalhe(reserva, detalhe):
        return ReservaDetalheRepository.create_reserva_detalhe(reserva, detalhe)

    @staticmethod
    def get_reserva_detalhe_by_uid(uid):
        return ReservaDetalheRepository.get_reserva_detalhe_by_uid(uid)

    @staticmethod
    def get_all_reserva_detalhes():
        return ReservaDetalheRepository.get_all_reserva_detalhes()

    @staticmethod
    def delete_reserva_detalhe(uid):
        return ReservaDetalheRepository.delete_reserva_detalhe(uid)
