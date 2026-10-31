kota = {
    "jakarta": {
        "negara": "indonesia",
        "populasi": "10 juta",
        "fakta": "Ibu kota Indonesia"
    },

    "tokyo": {
        "negara": "jepang",
        "populasi": "14 juta",
        "fakta": "Kota terbesar di Jepang"
    },

    "paris": {
        "negara": "prancis",
        "populasi": "2 juta",
        "fakta": "Terkenal dengan Menara Eiffel"
    }
}

for nama_kota, informasi in kota.items():
    print(f"\nKota: {nama_kota.title()}")
    print(f"Negara: {informasi['negara'].title()}")
    print(f"Populasi: {informasi['populasi']}")
    print(f"Fakta: {informasi['fakta']}")
    
#59