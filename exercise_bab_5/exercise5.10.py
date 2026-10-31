daftar_pengguna = [ "admin", "reev", "andi", "budi", "sinta"]

for pengguna in daftar_pengguna:
    if pengguna == "admin":
        print(
            "Halo admin, apakah Anda ingin melihat laporan status?"
        )
    else:
        print(
            f"Halo {pengguna}, terima kasih telah login kembali."
        )
        
print("=" * 50)
        
daftar_pengguna = []

if daftar_pengguna:
    for pengguna in daftar_pengguna:
        print(
            f"Halo {pengguna}, terima kasih telah login kembali."
        )
else:
    print("Kita perlu mencari beberapa pengguna!")
    
print("=" * 50)

pengguna_saat_ini = [
    "admin",
    "reev",
    "andi",
    "budi",
    "sinta"
]

pengguna_baru = [
    "Reev",
    "Joko",
    "SINTA",
    "Dewi",
    "Rizki"
]

pengguna_saat_ini_lower = []

for pengguna in pengguna_saat_ini:
    pengguna_saat_ini_lower.append(
        pengguna.lower()
    )

for pengguna in pengguna_baru:
    if pengguna.lower() in pengguna_saat_ini_lower:
        print(
            f"Nama pengguna '{pengguna}' sudah digunakan."
        )
        print("Silakan masukkan nama pengguna baru.\n")
    else:
        print(
            f"Nama pengguna '{pengguna}' tersedia.\n"
        )