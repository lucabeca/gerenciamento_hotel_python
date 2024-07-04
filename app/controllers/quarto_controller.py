from flask import Blueprint, request, jsonify
from services.quarto_service import QuartoService

quarto_blueprint = Blueprint('quarto_blueprint', __name__)

@quarto_blueprint.route('/', methods=['POST'])
def create_quarto():
    data = request.get_json()
    quarto = QuartoService.create_quarto(data['numero'], data['tipo'], data['capacidade'], data['hotel'])
    return jsonify(quarto.__dict__), 201

@quarto_blueprint.route('/<uid>', methods=['GET'])
def get_quarto(uid):
    quarto = QuartoService.get_quarto_by_uid(uid)
    if quarto:
        return jsonify(quarto.__dict__), 200
    return jsonify({'message': 'Quarto não encontrado'}), 404

@quarto_blueprint.route('/', methods=['GET'])
def get_all_quartos():
    quartos = QuartoService.get_all_quartos()
    return jsonify([quarto.__dict__ for quarto in quartos]), 200

@quarto_blueprint.route('/<uid>', methods=['DELETE'])
def delete_quarto(uid):
    if QuartoService.delete_quarto(uid):
        return jsonify({'message': 'Quarto deletado com sucesso'}), 200
    return jsonify({'message': 'Quarto não encontrado'}), 404
