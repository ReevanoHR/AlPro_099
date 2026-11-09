import json

nama_file = "username.json"

try:
    with open(nama_file) as file:
        username = json.load(file)

except FileNotFoundError:
    username = input(
        "Masukkan nama Anda: "
    )

    with open(
        nama_file,
        "w"
    ) as file:
        json.dump(
            username,
            file
        )

else:
    konfirmasi = input(
        f"Apakah Anda {username}? "
        "(y/t): "
    )

    if konfirmasi == "y":
        print(
            f"Selamat datang kembali, "
            f"{username}!"
        )
    else:
        username = input(
            "Masukkan nama yang benar: "
        )

        with open(
            nama_file,
            "w"
        ) as file:

            json.dump(
                username,
                file
            )