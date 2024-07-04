from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class Endereco(StructuredNode):
    uid = UniqueIdProperty()
    rua = StringProperty(required=True)
    cidade = StringProperty(required=True)
    estado = StringProperty(required=True)
    cep = StringProperty(required=True)
