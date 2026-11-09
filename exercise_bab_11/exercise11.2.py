import unittest
from exercise11Modul2 import city_country


class CityCountryTestCase(
    unittest.TestCase
):

    def test_city_country(self):
        hasil = city_country(
            "surakarta",
            "indonesia"
        )

        self.assertEqual(
            hasil,
            "Surakarta, Indonesia"
        )

    def test_city_country_population(
        self
    ):
        hasil = city_country(
            "surakarta",
            "indonesia",
            600000
        )

        self.assertEqual(
            hasil,
            "Surakarta, Indonesia - population 600000"
        )


unittest.main()