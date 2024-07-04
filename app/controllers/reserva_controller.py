from flask import Blueprint, request, jsonify
from repositories.reserva_repository import ReservaRepository

reserva_blueprint = Blueprint('reserva_blueprint', __name__)

@reserva_blueprint.route('/reservas', methods=['POST'])
def create_reserva():
    data = request.get_json()
    reserva = ReservaRepository.create_reserva(data['data_inicio'], data['data_fim'], data['forma_pagamento'])
    return jsonify(reserva.__properties__), 201

@reserva_blueprint.route('/reservas/<uid>', methods=['DELETE'])
def delete_reserva(uid):
    success = ReservaRepository.delete_reserva(uid)
    if success:
        return jsonify({"message": "Reserva deletada com sucesso"}), 200
    else:
        return jsonify({"message": "Reserva não encontrada"}), 404

@reserva_blueprint.route('/reservas', methods=['GET'])
def get_all_reservas():
    reservas = ReservaRepository.get_all_reservas()
    return jsonify([reserva.__properties__ for reserva in reservas]), 200

@reserva_blueprint.route('/reservas/<uid>', methods=['GET'])
def get_reserva(uid):
    reserva = ReservaRepository.get_reserva_by_uid(uid)
    if reserva:
        return jsonify(reserva.__properties__), 200
    else:
        return jsonify({"message": "Reserva não encontrada"}), 404
