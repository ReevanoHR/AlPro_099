def buat_sandwich(
    *isi_sandwich
):
    print(
        "\nSandwich dengan isi:"
    )

    for isi in isi_sandwich:
        print(f"- {isi}")

buat_sandwich(
    "ayam",
    "keju"
)

buat_sandwich(
    "telur",
    "selada",
    "tomat"
)