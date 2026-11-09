import json

nama_file = "username.json"

try:
    with open(nama_file) as file:
        username = json.load(file)

except FileNotFoundError:
    username = input(
        "Siapa nama Anda? "
    )

    with open(
        nama_file,
        "w"
    ) as file:

        json.dump(
            username,
            file
        )

    print(
        f"Kami akan mengingat Anda, "
        f"{username}."
    )
else:
    print(
        f"Selamat datang kembali, "
        f"{username}!"
    )