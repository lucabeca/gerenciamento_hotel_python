import unittest
from repositories.hotel_repository import HotelRepository
from neomodel import db

class HotelRepositoryTest(unittest.TestCase):

    def setUp(self):
        db.cypher_query("MATCH (n) DETACH DELETE n")

    def test_create_hotel(self):
        hotel = HotelRepository.create_hotel(nome="Hotel ABC", endereco="Endereco XYZ")
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.nome, "Hotel ABC")
        self.assertEqual(hotel.endereco, "Endereco XYZ")

    def test_get_hotel_by_uid(self):
        hotel = HotelRepository.create_hotel(nome="Hotel ABC", endereco="Endereco XYZ")
        retrieved_hotel = HotelRepository.get_hotel_by_uid(hotel.uid)
        self.assertIsNotNone(retrieved_hotel)
        self.assertEqual(retrieved_hotel.uid, hotel.uid)

    def test_get_all_hotels(self):
        HotelRepository.create_hotel(nome="Hotel ABC", endereco="Endereco XYZ")
        hotels = HotelRepository.get_all_hotels()
        self.assertGreaterEqual(len(hotels), 1)

    def test_delete_hotel(self):
        hotel = HotelRepository.create_hotel(nome="Hotel ABC", endereco="Endereco XYZ")
        self.assertTrue(HotelRepository.delete_hotel(hotel.uid))
        self.assertIsNone(HotelRepository.get_hotel_by_uid(hotel.uid))

if __name__ == '__main__':
    unittest.main()
