from models.tipo_quarto import TipoQuarto

class TipoQuartoRepository:

    @staticmethod
    def create_tipo_quarto(descricao):
        tipo_quarto = TipoQuarto(descricao=descricao).save()
        return tipo_quarto

    @staticmethod
    def get_tipo_quarto_by_uid(uid):
        try:
            tipo_quarto = TipoQuarto.nodes.get(uid=uid)
            return tipo_quarto
        except TipoQuarto.DoesNotExist:
            return None

    @staticmethod
    def get_all_tipo_quartos():
        return TipoQuarto.nodes.all()

    @staticmethod
    def delete_tipo_quarto(uid):
        tipo_quarto = TipoQuartoRepository.get_tipo_quarto_by_uid(uid)
        if tipo_quarto:
            tipo_quarto.delete()
            return True
        return False
