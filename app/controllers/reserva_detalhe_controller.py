from flask import Blueprint, request, jsonify
from repositories.reserva_detalhe_repository import ReservaDetalheRepository

reserva_detalhe_blueprint = Blueprint('reserva_detalhe_blueprint', __name__)

@reserva_detalhe_blueprint.route('/reservas_detalhe', methods=['POST'])
def create_reserva_detalhe():
    data = request.get_json()
    reserva_detalhe = ReservaDetalheRepository.create_reserva_detalhe(data['reserva_uid'], data['quarto_uid'], data['cliente_uid'])
    return jsonify(reserva_detalhe.__properties__), 201

@reserva_detalhe_blueprint.route('/reservas_detalhe/<uid>', methods=['DELETE'])
def delete_reserva_detalhe(uid):
    success = ReservaDetalheRepository.delete_reserva_detalhe(uid)
    if success:
        return jsonify({"message": "Detalhe de reserva deletado com sucesso"}), 200
    else:
        return jsonify({"message": "Detalhe de reserva não encontrado"}), 404

@reserva_detalhe_blueprint.route('/reservas_detalhe', methods=['GET'])
def get_all_reserva_detalhes():
    reserva_detalhes = ReservaDetalheRepository.get_all_reserva_detalhes()
    return jsonify([reserva_detalhe.__properties__ for reserva_detalhe in reserva_detalhes]), 200

@reserva_detalhe_blueprint.route('/reservas_detalhe/<uid>', methods=['GET'])
def get_reserva_detalhe(uid):
    reserva_detalhe = ReservaDetalheRepository.get_reserva_detalhe_by_uid(uid)
    if reserva_detalhe:
        return jsonify(reserva_detalhe.__properties__), 200
    else:
        return jsonify({"message": "Detalhe de reserva não encontrado"}), 404
