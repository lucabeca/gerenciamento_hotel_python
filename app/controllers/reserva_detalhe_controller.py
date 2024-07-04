from flask import Blueprint, request, jsonify
from services.reserva_detalhe_service import ReservaDetalheService

reserva_detalhe_blueprint = Blueprint('reserva_detalhe_blueprint', __name__)

@reserva_detalhe_blueprint.route('/', methods=['POST'])
def create_reserva_detalhe():
    data = request.get_json()
    reserva_detalhe = ReservaDetalheService.create_reserva_detalhe(data['reserva'], data['detalhe'])
    return jsonify(reserva_detalhe.__dict__), 201

@reserva_detalhe_blueprint.route('/<uid>', methods=['GET'])
def get_reserva_detalhe(uid):
    reserva_detalhe = ReservaDetalheService.get_reserva_detalhe_by_uid(uid)
    if reserva_detalhe:
        return jsonify(reserva_detalhe.__dict__), 200
    return jsonify({'message': 'Detalhe da reserva não encontrado'}), 404

@reserva_detalhe_blueprint.route('/', methods=['GET'])
def get_all_reserva_detalhes():
    reserva_detalhes = ReservaDetalheService.get_all_reserva_detalhes()
    return jsonify([reserva_detalhe.__dict__ for reserva_detalhe in reserva_detalhes]), 200

@reserva_detalhe_blueprint.route('/<uid>', methods=['DELETE'])
def delete_reserva_detalhe(uid):
    if ReservaDetalheService.delete_reserva_detalhe(uid):
        return jsonify({'message': 'Detalhe da reserva deletado com sucesso'}), 200
    return jsonify({'message': 'Detalhe da reserva não encontrado'}), 404
