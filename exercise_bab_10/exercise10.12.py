import json

try:
    with open(
        "angka_favorit.json"
    ) as file:

        angka = json.load(file)

except FileNotFoundError:
    angka = input(
        "Masukkan angka favorit: "
    )

    with open(
        "angka_favorit.json",
        "w"
    ) as file:

        json.dump(
            angka,
            file
        )

else:
    print(
        f"Saya tahu angka favorit Anda "
        f"adalah {angka}."
    )