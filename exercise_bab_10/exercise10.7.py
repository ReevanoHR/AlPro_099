while True:
    try:
        angka_1 = input(
            "Angka pertama (q untuk keluar): "
        )

        if angka_1 == "q":
            break

        angka_2 = input(
            "Angka kedua: "
        )

        hasil = int(angka_1) + int(angka_2)

        print(
            f"Hasil penjumlahan: {hasil}"
        )

    except ValueError:
        print(
            "Masukkan angka yang valid."
        )
