from neomodel import StructuredNode, StringProperty, UniqueIdProperty

class TipoQuarto(StructuredNode):
    uid = UniqueIdProperty()
    descricao = StringProperty(unique_index=True, required=True)
