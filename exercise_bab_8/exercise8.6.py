def format_kota(kota, negara):
    return f"{kota.title()}, {negara.title()}"

lokasi = format_kota(
    "surakarta",
    "indonesia"
)

print(lokasi)