from flask import Blueprint, request, jsonify
from repositories.quarto_repository import QuartoRepository

quarto_controller = Blueprint('quarto_controller', __name__)

@quarto_controller.route('/quartos/create', methods=['POST'])
def create_quarto():
    data = request.get_json()
    quarto = QuartoRepository.create_quarto(**data)
    return jsonify(quarto), 201

@quarto_controller.route('/quartos/<uid>', methods=['GET'])
def get_quarto(uid):
    quarto = QuartoRepository.get_quarto_by_uid(uid)
    return jsonify(quarto), 200

@quarto_controller.route('/quartos/all', methods=['GET'])
def get_all_quartos():
    quartos = QuartoRepository.get_all_quartos()
    return jsonify(quartos), 200

@quarto_controller.route('/quartos/delete/<uid>', methods=['DELETE'])
def delete_quarto(uid):
    QuartoRepository.delete_quarto(uid)
    return '', 200
