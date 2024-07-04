from flask import Blueprint, request, jsonify
from repositories.hotel_repository import HotelRepository

hotel_blueprint = Blueprint('hotel_blueprint', __name__)

@hotel_blueprint.route('/create', methods=['POST'])
def create_hotel():
    data = request.get_json()
    hotel = HotelRepository.create_hotel(**data)
    return jsonify(hotel.to_dict()), 201

@hotel_blueprint.route('/<uid>', methods=['GET'])
def get_hotel(uid):
    hotel = HotelRepository.get_hotel_by_uid(uid)
    if hotel:
        return jsonify(hotel.to_dict())
    return jsonify({'error': 'Hotel não encontrado'}), 404

@hotel_blueprint.route('/all', methods=['GET'])
def get_all_hotels():
    hotels = HotelRepository.get_all_hotels()
    return jsonify([hotel.to_dict() for hotel in hotels])

@hotel_blueprint.route('/delete/<uid>', methods=['DELETE'])
def delete_hotel(uid):
    success = HotelRepository.delete_hotel(uid)
    if success:
        return jsonify({'message': 'Hotel deletado com sucesso'})
    return jsonify({'error': 'Hotel não encontrado'}), 404
