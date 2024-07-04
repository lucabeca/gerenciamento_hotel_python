from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class Cliente(StructuredNode):
    uid = UniqueIdProperty()
    nome = StringProperty(required=True)
    email = StringProperty(unique_index=True, required=True)
    telefone = StringProperty(required=True)
