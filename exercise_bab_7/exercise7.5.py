while True:
    umur = input(
        "Masukkan umur Anda (ketik 'quit' untuk keluar): "
    )

    if umur == "quit":
        break

    umur = int(umur)

    if umur < 3:
        print("Tiket gratis.")
    elif umur <= 12:
        print("Harga tiket $10.")
    else:
        print("Harga tiket $15.")

#65