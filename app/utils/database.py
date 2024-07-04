from py2neo import Graph
from config import Config

class Database:
    def __init__(self):
        self.graph = Graph(Config.NEO4J_URI, auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD))

    def get_graph(self):
        return self.graph

# Instancia única do banco de dados
db = Database().get_graph()
