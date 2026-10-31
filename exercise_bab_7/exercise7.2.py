jumlah_orang = int(
    input("Berapa jumlah orang dalam rombongan Anda? ")
)

if jumlah_orang > 8:
    print("Maaf, Anda harus menunggu meja tersedia.")
else:
    print("Meja sudah tersedia untuk Anda.")