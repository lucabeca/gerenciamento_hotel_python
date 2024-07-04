import logging
import unittest
from neomodel import config
from config import Config

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Configurar neomodel
config.DATABASE_URL = Config.DATABASE_URL

def test_connection():
    from utils.database import db
    try:
        logging.info("Testando conexão com Neo4j...")
        result = db.run("MATCH (n) RETURN n LIMIT 1").data()
        print("Conexão com Neo4j estabelecida com sucesso!")
        # print("Resultado da consulta de teste:", result)
    except Exception as e:
        print(f"Falha ao conectar com Neo4j: {e}")

def run_tests():
    # Descobrir e executar os testes
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    test_connection()
    # run_tests()
    from menu import executaMenu
    executaMenu()
    