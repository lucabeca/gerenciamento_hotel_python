from datetime import datetime
from flask import Blueprint, request, jsonify
from services.reserva_service import ReservaService

reserva_blueprint = Blueprint('reserva_blueprint', __name__)

@reserva_blueprint.route('/', methods=['POST'])
def create_reserva():
    data = request.get_json()
    data_inicio = datetime.strptime(data['data_inicio'], '%Y-%m-%d').date()
    data_fim = datetime.strptime(data['data_fim'], '%Y-%m-%d').date()
    reserva = ReservaService.create_reserva(data_inicio, data_fim, data['cliente'], data['quarto'])
    return jsonify(reserva.__dict__), 201

@reserva_blueprint.route('/<uid>', methods=['GET'])
def get_reserva(uid):
    reserva = ReservaService.get_reserva_by_uid(uid)
    if reserva:
        return jsonify(reserva.__dict__), 200
    return jsonify({'message': 'Reserva não encontrada'}), 404

@reserva_blueprint.route('/', methods=['GET'])
def get_all_reservas():
    reservas = ReservaService.get_all_reservas()
    return jsonify([reserva.__dict__ for reserva in reservas]), 200

@reserva_blueprint.route('/<uid>', methods=['DELETE'])
def delete_reserva(uid):
    if ReservaService.delete_reserva(uid):
        return jsonify({'message': 'Reserva deletada com sucesso'}), 200
    return jsonify({'message': 'Reserva não encontrada'}), 404
