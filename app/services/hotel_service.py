from repositories.hotel_repository import HotelRepository

class HotelService:

    @staticmethod
    def create_hotel(nome, endereco):
        return HotelRepository.create_hotel(nome, endereco)

    @staticmethod
    def get_hotel_by_uid(uid):
        return HotelRepository.get_hotel_by_uid(uid)

    @staticmethod
    def get_all_hotels():
        return HotelRepository.get_all_hotels()

    @staticmethod
    def delete_hotel(uid):
        return HotelRepository.delete_hotel(uid)
