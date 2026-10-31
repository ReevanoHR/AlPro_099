tempat_favorit = {
    "Reevano": ["pantai", "gunung", "air terjun"],
    "Nizar": [
        "perpustakaan",
        "kampus",
        "museum"
    ],
    "citra": [
        "mall",
        "taman kota",
        "kebun binatang"
    ]
}

for nama, tempat in tempat_favorit.items():
    print(f"\nTempat favorit {nama.title()}:")

    for lokasi in tempat:
        print(f"- {lokasi.title()}")
        
#60