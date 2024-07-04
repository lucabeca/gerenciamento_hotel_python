from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class Hotel(StructuredNode):
    uid = UniqueIdProperty()
    nome = StringProperty(unique_index=True, required=True)
    endereco = StringProperty(required=True)
