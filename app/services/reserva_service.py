from repositories.reserva_repository import ReservaRepository

class ReservaService:

    @staticmethod
    def create_reserva(data_inicio, data_fim, cliente, quarto):
        return ReservaRepository.create_reserva(data_inicio, data_fim, cliente, quarto)

    @staticmethod
    def get_reserva_by_uid(uid):
        return ReservaRepository.get_reserva_by_uid(uid)

    @staticmethod
    def get_all_reservas():
        return ReservaRepository.get_all_reservas()

    @staticmethod
    def delete_reserva(uid):
        return ReservaRepository.delete_reserva(uid)
