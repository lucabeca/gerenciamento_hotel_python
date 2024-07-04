from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty

class Quarto(StructuredNode):
    uid = UniqueIdProperty()
    numero = StringProperty(unique_index=True, required=True)
    tipo = StringProperty(required=True)
    capacidade = IntegerProperty(required=True)
    hotel = StringProperty(required=True)
