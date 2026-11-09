import json

angka_favorit = input(
    "Masukkan angka favorit Anda: "
)

with open(
    "angka_favorit.json",
    "w"
) as file:
    json.dump(
        angka_favorit,
        file
    )

print(
    "Angka favorit telah disimpan."
)