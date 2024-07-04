from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class ReservaDetalhe(StructuredNode):
    uid = UniqueIdProperty()
    reserva = StringProperty(required=True)
    detalhe = StringProperty(required=True)
