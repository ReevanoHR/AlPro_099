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