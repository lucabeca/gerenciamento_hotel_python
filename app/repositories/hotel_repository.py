from models.hotel import Hotel

class HotelRepository:

    @staticmethod
    def create_hotel(nome, endereco):
        hotel = Hotel(nome=nome, endereco=endereco).save()
        return hotel

    @staticmethod
    def get_hotel_by_uid(uid):
        try:
            hotel = Hotel.nodes.get(uid=uid)
            return hotel
        except Hotel.DoesNotExist:
            return None

    @staticmethod
    def get_all_hotels():
        return Hotel.nodes.all()

    @staticmethod
    def delete_hotel(uid):
        hotel = HotelRepository.get_hotel_by_uid(uid)
        if hotel:
            hotel.delete()
            return True
        return False
