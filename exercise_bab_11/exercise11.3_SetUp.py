import unittest
from exercise11Modul3 import Employee


class TestEmployee(
    unittest.TestCase
):

    def setUp(self):
        self.pegawai = Employee(
            "Budi",
            "Santoso",
            50000
        )

    def test_default_raise(
        self
    ):
        self.pegawai.give_raise()

        self.assertEqual(
            self.pegawai.gaji,
            55000
        )

    def test_custom_raise(
        self
    ):
        self.pegawai.give_raise(
            10000
        )

        self.assertEqual(
            self.pegawai.gaji,
            60000
        )


unittest.main()