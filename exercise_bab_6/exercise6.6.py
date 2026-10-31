orang_favorit = {
    "Reevano": "python",
    "Nizar": "java",
    "Raka": "python",
    "Sergie": "c++"
}

responden = [
    "Reevano",
    "Nizar",
    "Raka",
    "Sergie",
    "Yusuf"
]

for orang in responden:
    if orang in orang_favorit:
        print(
            f"Terima kasih {orang.title()} "
            "telah mengikuti survei."
        )
    else:
        print(
            f"{orang.title()}, "
            "silakan ikuti survei bahasa pemrograman."
        )