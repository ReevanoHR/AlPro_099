def buat_album(
    penyanyi,
    judul_album
):
    album = {
        "penyanyi": penyanyi,
        "judul": judul_album
    }

    return album

album = buat_album(
    "Tulus",
    "Monokrom"
)

print(album)
