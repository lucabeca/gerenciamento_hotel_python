from flask import Blueprint, request, jsonify
from repositories.endereco_repository import EnderecoRepository

endereco_blueprint = Blueprint('endereco_blueprint', __name__)

@endereco_blueprint.route('/create', methods=['POST'])
def create_endereco():
    data = request.get_json()
    endereco = EnderecoRepository.create_endereco(**data)
    return jsonify(endereco.to_dict()), 201

@endereco_blueprint.route('/<uid>', methods=['GET'])
def get_endereco(uid):
    endereco = EnderecoRepository.get_endereco_by_uid(uid)
    if endereco:
        return jsonify(endereco.to_dict())
    return jsonify({'error': 'Endereço não encontrado'}), 404

@endereco_blueprint.route('/all', methods=['GET'])
def get_all_enderecos():
    enderecos = EnderecoRepository.get_all_enderecos()
    return jsonify([endereco.to_dict() for endereco in enderecos])

@endereco_blueprint.route('/delete/<uid>', methods=['DELETE'])
def delete_endereco(uid):
    success = EnderecoRepository.delete_endereco(uid)
    if success:
        return jsonify({'message': 'Endereço deletado com sucesso'})
    return jsonify({'error': 'Endereço não encontrado'}), 404
