class Config:
    NEO4J_URI = 'bolt://localhost:7687'
    NEO4J_USERNAME = 'neo4j'
    NEO4J_PASSWORD = 'trabalho'
    DATABASE_URL = f'bolt://{NEO4J_USERNAME}:{NEO4J_PASSWORD}@localhost:7687'
