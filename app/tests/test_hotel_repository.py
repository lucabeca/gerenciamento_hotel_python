import unittest
from models import Hotel
from repositories.hotel_repository import HotelRepository

class HotelRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.hotel_data = {
            "nome": "Hotel Teste",
            "classificacao": 5,
            "data_construcao": "2020-01-01",
            "quantidade_quartos": 100
        }
        self.hotel = HotelRepository.create_hotel(**self.hotel_data)

    def tearDown(self):
        HotelRepository.delete_hotel(self.hotel.uid)

    def test_create_hotel(self):
        self.assertIsNotNone(self.hotel)
        self.assertEqual(self.hotel.nome, self.hotel_data["nome"])
        self.assertEqual(self.hotel.classificacao, self.hotel_data["classificacao"])

    def test_delete_hotel(self):
        self.assertTrue(HotelRepository.delete_hotel(self.hotel.uid))

    def test_get_all_hotels(self):
        hoteis = HotelRepository.get_all_hotels()
        self.assertGreater(len(hoteis), 0)

    def test_get_hotel_by_uid(self):
        hotel = HotelRepository.get_hotel_by_uid(self.hotel.uid)
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.uid, self.hotel.uid)

if __name__ == '__main__':
    unittest.main()
