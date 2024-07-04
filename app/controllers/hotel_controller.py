from flask import Blueprint, request, jsonify
from services.hotel_service import HotelService

hotel_blueprint = Blueprint('hotel_blueprint', __name__)

@hotel_blueprint.route('/', methods=['POST'])
def create_hotel():
    data = request.get_json()
    hotel = HotelService.create_hotel(data['nome'], data['endereco'])
    return jsonify(hotel.__dict__), 201

@hotel_blueprint.route('/<uid>', methods=['GET'])
def get_hotel(uid):
    hotel = HotelService.get_hotel_by_uid(uid)
    if hotel:
        return jsonify(hotel.__dict__), 200
    return jsonify({'message': 'Hotel não encontrado'}), 404

@hotel_blueprint.route('/', methods=['GET'])
def get_all_hotels():
    hoteis = HotelService.get_all_hotels()
    return jsonify([hotel.__dict__ for hotel in hoteis]), 200

@hotel_blueprint.route('/<uid>', methods=['DELETE'])
def delete_hotel(uid):
    if HotelService.delete_hotel(uid):
        return jsonify({'message': 'Hotel deletado com sucesso'}), 200
    return jsonify({'message': 'Hotel não encontrado'}), 404
