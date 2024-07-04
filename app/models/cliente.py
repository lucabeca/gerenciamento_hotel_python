from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class Cliente(StructuredNode):
    uid = UniqueIdProperty()
    nome = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)
