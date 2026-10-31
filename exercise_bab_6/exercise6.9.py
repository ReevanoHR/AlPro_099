tempat_favorit = {
    "Reevano": ["pantai", "gunung"],
    "Nizar": ["perpustakaan", "kampus"],
    "Raka": ["mall", "taman kota"]
}

for nama, tempat in tempat_favorit.items():
    print(f"\nTempat favorit {nama.title()}:")

    for lokasi in tempat:
        print(f"- {lokasi.title()}")