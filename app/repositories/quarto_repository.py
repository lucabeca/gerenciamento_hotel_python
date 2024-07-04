from models.quarto import Quarto

class QuartoRepository:

    @staticmethod
    def create_quarto(numero, tipo, capacidade, hotel):
        quarto = Quarto(numero=numero, tipo=tipo, capacidade=capacidade, hotel=hotel).save()
        return quarto

    @staticmethod
    def get_quarto_by_uid(uid):
        try:
            quarto = Quarto.nodes.get(uid=uid)
            return quarto
        except Quarto.DoesNotExist:
            return None

    @staticmethod
    def get_all_quartos():
        return Quarto.nodes.all()

    @staticmethod
    def delete_quarto(uid):
        quarto = QuartoRepository.get_quarto_by_uid(uid)
        if quarto:
            quarto.delete()
            return True
        return False
