import unittest
from exercise11Modul1 import city_country


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        hasil = city_country(
            "surakarta",
            "indonesia"
        )

        self.assertEqual(
            hasil,
            "Surakarta, Indonesia"
        )


unittest.main()