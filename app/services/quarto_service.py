from repositories.quarto_repository import QuartoRepository

class QuartoService:

    @staticmethod
    def create_quarto(numero, tipo, capacidade, hotel):
        return QuartoRepository.create_quarto(numero, tipo, capacidade, hotel)

    @staticmethod
    def get_quarto_by_uid(uid):
        return QuartoRepository.get_quarto_by_uid(uid)

    @staticmethod
    def get_all_quartos():
        return QuartoRepository.get_all_quartos()

    @staticmethod
    def delete_quarto(uid):
        return QuartoRepository.delete_quarto(uid)
