sungai = {
    "nil": "mesir",
    "amazon": "brazil",
    "bengawan solo": "indonesia"
}

for nama_sungai, negara in sungai.items():
    print(f"Sungai {nama_sungai.title()} mengalir di {negara.title()}.")

print()

for nama_sungai in sungai.keys():
    print(nama_sungai.title())

print()

for negara in sungai.values():
    print(negara.title())
    
#53