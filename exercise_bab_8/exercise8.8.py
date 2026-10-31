while True:
    penyanyi = input(
        "Nama penyanyi (q untuk keluar): "
    )

    if penyanyi == "q":
        break

    album = input(
        "Judul album: "
    )

    data_album = buat_album(
        penyanyi,
        album
    )

    print(data_album)