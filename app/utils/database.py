import os
from py2neo import Graph
from config import Config
from neomodel import config as neomodel_config

# Configurando o Neomodel com as mesmas credenciais
neomodel_config.DATABASE_URL = f"bolt://{Config.NEO4J_USERNAME}:{Config.NEO4J_PASSWORD}@{Config.NEO4J_URI.split('://')[1]}"

class Database:
    def __init__(self):
        self.graph = Graph(Config.NEO4J_URI, auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD))

    def get_graph(self):
        return self.graph

db = Database().get_graph()