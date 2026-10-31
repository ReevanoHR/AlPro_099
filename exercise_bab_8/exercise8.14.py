def buat_mobil(
    pabrikan,
    model,
    **informasi
):
    mobil = {
        "pabrikan": pabrikan,
        "model": model
    }

    for kunci, nilai in (
        informasi.items()
    ):
        mobil[kunci] = nilai

    return mobil

mobil = buat_mobil(
    "Toyota",
    "Avanza",
    warna="Hitam",
    tahun=2024
)

print(mobil)