from flask import Blueprint, request, jsonify
from services.endereco_service import EnderecoService

endereco_blueprint = Blueprint('endereco_blueprint', __name__)

@endereco_blueprint.route('/', methods=['POST'])
def create_endereco():
    data = request.get_json()
    endereco = EnderecoService.create_endereco(data['rua'], data['cidade'], data['estado'], data['cep'])
    return jsonify(endereco.__dict__), 201

@endereco_blueprint.route('/<uid>', methods=['GET'])
def get_endereco(uid):
    endereco = EnderecoService.get_endereco_by_uid(uid)
    if endereco:
        return jsonify(endereco.__dict__), 200
    return jsonify({'message': 'Endereço não encontrado'}), 404

@endereco_blueprint.route('/', methods=['GET'])
def get_all_enderecos():
    enderecos = EnderecoService.get_all_enderecos()
    return jsonify([endereco.__dict__ for endereco in enderecos]), 200

@endereco_blueprint.route('/<uid>', methods=['DELETE'])
def delete_endereco(uid):
    if EnderecoService.delete_endereco(uid):
        return jsonify({'message': 'Endereço deletado com sucesso'}), 200
    return jsonify({'message': 'Endereço não encontrado'}), 404
