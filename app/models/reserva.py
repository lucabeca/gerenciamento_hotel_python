from neomodel import StructuredNode, StringProperty, DateProperty, UniqueIdProperty

class Reserva(StructuredNode):
    uid = UniqueIdProperty()
    data_inicio = DateProperty(required=True)
    data_fim = DateProperty(required=True)
    cliente = StringProperty(required=True)
    quarto = StringProperty(required=True)
