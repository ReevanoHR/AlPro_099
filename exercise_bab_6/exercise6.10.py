angka_favorit = {
    "Reevano": [7, 17],
    "Nizar": [10, 20],
    "Raka": [3, 13],
    "Sergie": [25, 50],
    "Yusuf": [9, 19]
}

for nama, angka in angka_favorit.items():
    print(f"\nAngka favorit {nama.title()}:")

    for nilai in angka:
        print(nilai)