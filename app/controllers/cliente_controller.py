from flask import Blueprint, request, jsonify
from repositories.cliente_repository import ClienteRepository

cliente_blueprint = Blueprint('cliente_blueprint', __name__)

@cliente_blueprint.route('/create', methods=['POST'])
def create_cliente():
    data = request.get_json()
    cliente = ClienteRepository.create_cliente(**data)
    return jsonify(cliente.to_dict()), 201

@cliente_blueprint.route('/<uid>', methods=['GET'])
def get_cliente(uid):
    cliente = ClienteRepository.get_cliente_by_uid(uid)
    if cliente:
        return jsonify(cliente.to_dict())
    return jsonify({'error': 'Cliente não encontrado'}), 404

@cliente_blueprint.route('/all', methods=['GET'])
def get_all_clientes():
    clientes = ClienteRepository.get_all_clientes()
    return jsonify([cliente.to_dict() for cliente in clientes])

@cliente_blueprint.route('/delete/<uid>', methods=['DELETE'])
def delete_cliente(uid):
    success = ClienteRepository.delete_cliente(uid)
    if success:
        return jsonify({'message': 'Cliente deletado com sucesso'})
    return jsonify({'error': 'Cliente não encontrado'}), 404
