from flask import Blueprint, request, jsonify
from services.tipo_quarto_service import TipoQuartoService

tipo_quarto_blueprint = Blueprint('tipo_quarto_blueprint', __name__)

@tipo_quarto_blueprint.route('/', methods=['POST'])
def create_tipo_quarto():
    data = request.get_json()
    tipo_quarto = TipoQuartoService.create_tipo_quarto(data['descricao'])
    return jsonify(tipo_quarto.__dict__), 201

@tipo_quarto_blueprint.route('/<uid>', methods=['GET'])
def get_tipo_quarto(uid):
    tipo_quarto = TipoQuartoService.get_tipo_quarto_by_uid(uid)
    if tipo_quarto:
        return jsonify(tipo_quarto.__dict__), 200
    return jsonify({'message': 'Tipo de quarto não encontrado'}), 404

@tipo_quarto_blueprint.route('/', methods=['GET'])
def get_all_tipo_quartos():
    tipo_quartos = TipoQuartoService.get_all_tipo_quartos()
    return jsonify([tipo_quarto.__dict__ for tipo_quarto in tipo_quartos]), 200

@tipo_quarto_blueprint.route('/<uid>', methods=['DELETE'])
def delete_tipo_quarto(uid):
    if TipoQuartoService.delete_tipo_quarto(uid):
        return jsonify({'message': 'Tipo de quarto deletado com sucesso'}), 200
    return jsonify({'message': 'Tipo de quarto não encontrado'}), 404
