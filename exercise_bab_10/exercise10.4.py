while True:
    nama = input(
        "Masukkan nama (ketik 'q' untuk keluar): "
    )

    if nama == "q":
        break

    with open("guest_book.txt", "a") as file:
        file.write(f"{nama}\n")

    print(f"Halo, {nama}!")