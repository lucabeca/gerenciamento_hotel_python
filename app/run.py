import sys
import os
import logging
from neomodel import config

# Configuração do logging
logging.basicConfig(level=logging.INFO)

try:
    from utils.database import db
    from config import Config

    # Configurar neomodel
    config.DATABASE_URL = Config.DATABASE_URL

    print("Importação do módulo 'app' bem-sucedida.")
except ModuleNotFoundError as e:
    print(f"Erro ao importar o módulo 'app': {e}")

def test_connection():
    try:
        logging.info("Testando conexão com Neo4j...")
        result = db.run("MATCH (n) RETURN n LIMIT 1").data()
        print("Conexão com Neo4j estabelecida com sucesso!")
        # print("Resultado da consulta de teste:", result)
    except Exception as e:
        print(f"Falha ao conectar com Neo4j: {e}")

def run_tests():
    import unittest
    # Adicionar os testes que você deseja executar
    from tests.test_cliente_repository import ClienteRepositoryTest
    from tests.test_endereco_repository import EnderecoRepositoryTest
    from tests.test_hotel_repository import HotelRepositoryTest
    from tests.test_quarto_repository import QuartoRepositoryTest
    from tests.test_reserva_repository import ReservaRepositoryTest
    from tests.test_reserva_detalhe_repository import ReservaDetalheRepositoryTest
    from tests.test_tipo_quarto_repository import TipoQuartoRepositoryTest

    # Executar todos os testes
    unittest.main()

if __name__ == "__main__":
    test_connection()
    run_tests()
