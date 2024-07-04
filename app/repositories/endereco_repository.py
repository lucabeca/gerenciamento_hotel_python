from models.endereco import Endereco

class EnderecoRepository:

    @staticmethod
    def create_endereco(rua, cidade, estado, cep):
        endereco = Endereco(rua=rua, cidade=cidade, estado=estado, cep=cep).save()
        return endereco

    @staticmethod
    def get_endereco_by_uid(uid):
        try:
            endereco = Endereco.nodes.get(uid=uid)
            return endereco
        except Endereco.DoesNotExist:
            return None

    @staticmethod
    def get_all_enderecos():
        return Endereco.nodes.all()

    @staticmethod
    def delete_endereco(uid):
        endereco = EnderecoRepository.get_endereco_by_uid(uid)
        if endereco:
            endereco.delete()
            return True
        return False
