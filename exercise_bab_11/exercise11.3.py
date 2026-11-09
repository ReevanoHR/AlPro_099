import unittest
from exercise11Modul3 import Employee


class TestEmployee(
    unittest.TestCase
):

    def test_default_raise(
        self
    ):
        pegawai = Employee(
            "Budi",
            "Santoso",
            50000
        )

        pegawai.give_raise()

        self.assertEqual(
            pegawai.gaji,
            55000
        )

    def test_custom_raise(
        self
    ):
        pegawai = Employee(
            "Budi",
            "Santoso",
            50000
        )

        pegawai.give_raise(
            10000
        )

        self.assertEqual(
            pegawai.gaji,
            60000
        )


unittest.main()