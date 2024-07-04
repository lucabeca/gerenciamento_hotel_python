from repositories.tipo_quarto_repository import TipoQuartoRepository

class TipoQuartoService:

    @staticmethod
    def create_tipo_quarto(descricao):
        return TipoQuartoRepository.create_tipo_quarto(descricao)

    @staticmethod
    def get_tipo_quarto_by_uid(uid):
        return TipoQuartoRepository.get_tipo_quarto_by_uid(uid)

    @staticmethod
    def get_all_tipo_quartos():
        return TipoQuartoRepository.get_all_tipo_quartos()

    @staticmethod
    def delete_tipo_quarto(uid):
        return TipoQuartoRepository.delete_tipo_quarto(uid)
