def buat_profil(
    nama_depan,
    nama_belakang,
    **informasi
):
    profil = {}

    profil[
        "nama_depan"
    ] = nama_depan

    profil[
        "nama_belakang"
    ] = nama_belakang

    for kunci, nilai in (
        informasi.items()
    ):
        profil[kunci] = nilai

    return profil

pengguna = buat_profil(
    "Budi",
    "Santoso",
    umur=18,
    kota="Surakarta"
)

print(pengguna)