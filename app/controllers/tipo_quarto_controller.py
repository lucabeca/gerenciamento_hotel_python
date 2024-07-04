from flask import Blueprint, request, jsonify
from repositories.tipo_quarto_repository import TipoQuartoRepository

tipo_quarto_blueprint = Blueprint('tipo_quarto_blueprint', __name__)

@tipo_quarto_blueprint.route('/tipos_quartos', methods=['POST'])
def create_tipo_quarto():
    data = request.get_json()
    tipo_quarto = TipoQuartoRepository.create_tipo_quarto(data['tipo'], data['capacidade'], data['descricao'])
    return jsonify(tipo_quarto.__properties__), 201

@tipo_quarto_blueprint.route('/tipos_quartos/<uid>', methods=['DELETE'])
def delete_tipo_quarto(uid):
    success = TipoQuartoRepository.delete_tipo_quarto(uid)
    if success:
        return jsonify({"message": "Tipo de quarto deletado com sucesso"}), 200
    else:
        return jsonify({"message": "Tipo de quarto não encontrado"}), 404

@tipo_quarto_blueprint.route('/tipos_quartos', methods=['GET'])
def get_all_tipo_quartos():
    tipos_quartos = TipoQuartoRepository.get_all_tipo_quartos()
    return jsonify([tipo_quarto.__properties__ for tipo_quarto in tipos_quartos]), 200

@tipo_quarto_blueprint.route('/tipos_quartos/<uid>', methods=['GET'])
def get_tipo_quarto(uid):
    tipo_quarto = TipoQuartoRepository.get_tipo_quarto_by_uid(uid)
    if tipo_quarto:
        return jsonify(tipo_quarto.__properties__), 200
    else:
        return jsonify({"message": "Tipo de quarto não encontrado"}), 404
