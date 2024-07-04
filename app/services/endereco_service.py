from repositories.endereco_repository import EnderecoRepository

class EnderecoService:

    @staticmethod
    def create_endereco(rua, cidade, estado, cep):
        return EnderecoRepository.create_endereco(rua, cidade, estado, cep)

    @staticmethod
    def get_endereco_by_uid(uid):
        return EnderecoRepository.get_endereco_by_uid(uid)

    @staticmethod
    def get_all_enderecos():
        return EnderecoRepository.get_all_enderecos()

    @staticmethod
    def delete_endereco(uid):
        return EnderecoRepository.delete_endereco(uid)
