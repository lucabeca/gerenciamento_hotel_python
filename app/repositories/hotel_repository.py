from neomodel import db
from models import Hotel

class HotelRepository:

    @staticmethod
    def create_hotel(nome, classificacao, data_construcao, quantidade_quartos):
        hotel = Hotel(nome=nome, classificacao=classificacao, data_construcao=data_construcao, quantidade_quartos=quantidade_quartos)
        hotel.save()
        return hotel

    @staticmethod
    def delete_hotel(uid):
        hotel = Hotel.nodes.get_or_none(uid=uid)
        if hotel:
            hotel.delete()
            return True
        return False

    @staticmethod
    def get_all_hotels():
        return Hotel.nodes.all()

    @staticmethod
    def get_hotel_by_uid(uid):
        return Hotel.nodes.get_or_none(uid=uid)
