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