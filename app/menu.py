import sys
from repositories.cliente_repository import ClienteRepository
from repositories.endereco_repository import EnderecoRepository
from repositories.hotel_repository import HotelRepository
from repositories.quarto_repository import QuartoRepository
from repositories.reserva_repository import ReservaRepository
from repositories.reserva_detalhe_repository import ReservaDetalheRepository
from repositories.tipo_quarto_repository import TipoQuartoRepository

def print_menu():
    print("Menu:")
    print("1. Gerenciar Clientes")
    print("2. Gerenciar Endereços")
    print("3. Gerenciar Hotéis")
    print("4. Gerenciar Quartos")
    print("5. Gerenciar Reservas")
    print("6. Gerenciar Detalhes de Reservas")
    print("7. Gerenciar Tipos de Quartos")
    print("8. Sair")

def gerenciar_clientes():
    while True:
        print("Gerenciar Clientes:")
        print("1. Criar Cliente")
        print("2. Deletar Cliente")
        print("3. Listar Todos os Clientes")
        print("4. Buscar Cliente por UID")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            ClienteRepository.create_cliente(nome, email)
            print("Cliente criado com sucesso!")

        elif opcao == '2':
            uid = input("Digite o UID do cliente a ser deletado: ")
            cliente = ClienteRepository.get_cliente_by_uid(uid)
            if cliente:
                sucesso = ClienteRepository.delete_cliente(uid)
                if sucesso:
                    print("Cliente deletado com sucesso!")
                else:
                    print("Erro ao deletar o cliente.")
            else:
                print("Cliente não encontrado. Tente novamente.")

        elif opcao == '3':
            clientes = ClienteRepository.get_all_clientes()
            for cliente in clientes:
                print(f"UID: {cliente.uid}, Nome: {cliente.nome}, Email: {cliente.email}")

        elif opcao == '4':
            uid = input("Digite o UID do cliente: ")
            cliente = ClienteRepository.get_cliente_by_uid(uid)
            if cliente:
                print(f"UID: {cliente.uid}, Nome: {cliente.nome}, Email: {cliente.email}")
            else:
                print("Cliente não encontrado. Tente novamente.")

        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")        

def gerenciar_enderecos():
    print("Gerenciar Endereços:")
    print("1. Criar Endereço")
    print("2. Deletar Endereço")
    print("3. Listar Todos os Endereços")
    print("4. Buscar Endereço por UID")
    print("5. Voltar ao Menu Principal")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        rua = input("Rua: ")
        numero = input("Número: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        ClienteRepository.create_endereco(rua, numero, cidade, estado)
        print("Endereço criado com sucesso!")
    elif choice == '2':
        uid = input("UID do Endereço: ")
        EnderecoRepository.delete_endereco(uid)
        print("Endereço deletado com sucesso!")
    elif choice == '3':
        enderecos = EnderecoRepository.get_all_enderecos()
        for endereco in enderecos:
            print(endereco)
    elif choice == '4':
        uid = input("UID do Endereço: ")
        endereco = EnderecoRepository.get_endereco_by_uid(uid)
        print(endereco)
    elif choice == '5':
        return
    else:
        print("Opção inválida, por favor tente novamente.")
    gerenciar_enderecos()

def gerenciar_hoteis():
    print("Gerenciar Hotéis:")
    print("1. Criar Hotel")
    print("2. Deletar Hotel")
    print("3. Listar Todos os Hotéis")
    print("4. Buscar Hotel por UID")
    print("5. Voltar ao Menu Principal")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        nome = input("Nome do Hotel: ")
        endereco_uid = input("UID do Endereço: ")
        HotelRepository.create_hotel(nome, endereco_uid)
        print("Hotel criado com sucesso!")
    elif choice == '2':
        uid = input("UID do Hotel: ")
        HotelRepository.delete_hotel(uid)
        print("Hotel deletado com sucesso!")
    elif choice == '3':
        hoteis = HotelRepository.get_all_hoteis()
        for hotel in hoteis:
            print(hotel)
    elif choice == '4':
        uid = input("UID do Hotel: ")
        hotel = HotelRepository.get_hotel_by_uid(uid)
        print(hotel)
    elif choice == '5':
        return
    else:
        print("Opção inválida, por favor tente novamente.")
    gerenciar_hoteis()

def gerenciar_quartos():
    print("Gerenciar Quartos:")
    print("1. Criar Quarto")
    print("2. Deletar Quarto")
    print("3. Listar Todos os Quartos")
    print("4. Buscar Quarto por UID")
    print("5. Voltar ao Menu Principal")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        numero = input("Número do Quarto: ")
        tipo_uid = input("UID do Tipo de Quarto: ")
        hotel_uid = input("UID do Hotel: ")
        QuartoRepository.create_quarto(numero, tipo_uid, hotel_uid)
        print("Quarto criado com sucesso!")
    elif choice == '2':
        uid = input("UID do Quarto: ")
        QuartoRepository.delete_quarto(uid)
        print("Quarto deletado com sucesso!")
    elif choice == '3':
        quartos = QuartoRepository.get_all_quartos()
        for quarto in quartos:
            print(quarto)
    elif choice == '4':
        uid = input("UID do Quarto: ")
        quarto = QuartoRepository.get_quarto_by_uid(uid)
        print(quarto)
    elif choice == '5':
        return
    else:
        print("Opção inválida, por favor tente novamente.")
    gerenciar_quartos()

def gerenciar_reservas():
    print("Gerenciar Reservas:")
    print("1. Criar Reserva")
    print("2. Deletar Reserva")
    print("3. Listar Todas as Reservas")
    print("4. Buscar Reserva por UID")
    print("5. Voltar ao Menu Principal")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        data_inicio = input("Data de Início (YYYY-MM-DD): ")
        data_fim = input("Data de Fim (YYYY-MM-DD): ")
        cliente_uid = input("UID do Cliente: ")
        quarto_uid = input("UID do Quarto: ")
        ReservaRepository.create_reserva(data_inicio, data_fim, cliente_uid, quarto_uid)
        print("Reserva criada com sucesso!")
    elif choice == '2':
        uid = input("UID da Reserva: ")
        ReservaRepository.delete_reserva(uid)
        print("Reserva deletada com sucesso!")
    elif choice == '3':
        reservas = ReservaRepository.get_all_reservas()
        for reserva in reservas:
            print(reserva)
    elif choice == '4':
        uid = input("UID da Reserva: ")
        reserva = ReservaRepository.get_reserva_by_uid(uid)
        print(reserva)
    elif choice == '5':
        return
    else:
        print("Opção inválida, por favor tente novamente.")
    gerenciar_reservas()

def gerenciar_reserva_detalhes():
    print("Gerenciar Detalhes de Reservas:")
    print("1. Criar Detalhe de Reserva")
    print("2. Deletar Detalhe de Reserva")
    print("3. Listar Todos os Detalhes de Reservas")
    print("4. Buscar Detalhe de Reserva por UID")
    print("5. Voltar ao Menu Principal")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        descricao = input("Descrição: ")
        valor = input("Valor: ")
        reserva_uid = input("UID da Reserva: ")
        ReservaDetalheRepository.create_reserva_detalhe(descricao, valor, reserva_uid)
        print("Detalhe de Reserva criado com sucesso!")
    elif choice == '2':
        uid = input("UID do Detalhe de Reserva: ")
        ReservaDetalheRepository.delete_reserva_detalhe(uid)
        print("Detalhe de Reserva deletado com sucesso!")
    elif choice == '3':
        detalhes = ReservaDetalheRepository.get_all_reserva_detalhes()
        for detalhe in detalhes:
            print(detalhe)
    elif choice == '4':
        uid = input("UID do Detalhe de Reserva: ")
        detalhe = ReservaDetalheRepository.get_reserva_detalhe_by_uid(uid)
        print(detalhe)
    elif choice == '5':
        return
    else:
        print("Opção inválida, por favor tente novamente.")
    gerenciar_reserva_detalhes()

def gerenciar_tipos_quarto():
    print("Gerenciar Tipos de Quartos:")
    print("1. Criar Tipo de Quarto")
    print("2. Deletar Tipo de Quarto")
    print("3. Listar Todos os Tipos de Quartos")
    print("4. Buscar Tipo de Quarto por UID")
    print("5. Voltar ao Menu Principal")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        nome = input("Nome do Tipo de Quarto: ")
        TipoQuartoRepository.create_tipo_quarto(nome)
        print("Tipo de Quarto criado com sucesso!")
    elif choice == '2':
        uid = input("UID do Tipo de Quarto: ")
        TipoQuartoRepository.delete_tipo_quarto(uid)
        print("Tipo de Quarto deletado com sucesso!")
    elif choice == '3':
        tipos = TipoQuartoRepository.get_all_tipo_quartos()
        for tipo in tipos:
            print(tipo)
    elif choice == '4':
        uid = input("UID do Tipo de Quarto: ")
        tipo = TipoQuartoRepository.get_tipo_quarto_by_uid(uid)
        print(tipo)
    elif choice == '5':
        return
    else:
        print("Opção inválida, por favor tente novamente.")
    gerenciar_tipos_quarto()

def executaMenu():
    while True:
        print_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            gerenciar_clientes()
        elif choice == '2':
            gerenciar_enderecos()
        elif choice == '3':
            gerenciar_hoteis()
        elif choice == '4':
            gerenciar_quartos()
        elif choice == '5':
            gerenciar_reservas()
        elif choice == '6':
            gerenciar_reserva_detalhes()
        elif choice == '7':
            gerenciar_tipos_quarto()
        elif choice == '8':
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida, por favor tente novamente.")
    
def deletar_cliente():
    uid = input("Digite o UID do cliente a ser deletado: ")
    if not uid:
        print("UID não fornecido. Não é possível deletar o cliente.")
        return
    resultado = ClienteRepository.delete_cliente(uid)
    if resultado:
        print("Cliente deletado com sucesso.")
    else:
        print("Erro ao deletar cliente. Verifique se o UID está correto.")

if __name__ == "__main__":
    executaMenu()
