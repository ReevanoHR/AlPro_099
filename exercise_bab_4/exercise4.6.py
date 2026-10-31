for angka in range(1, 21):
    print(angka)
    
print("=" * 50)

daftar_angka = list(range(1, 1_000_001))

for angka in daftar_angka:
    print(angka)
    
print("=" * 50)

print("Nilai terkecil:", min(daftar_angka))
print("Nilai terbesar:", max(daftar_angka))
print("Jumlah seluruh angka:", sum(daftar_angka))

print("=" * 50)

angka_ganjil = range(1, 21, 2)

for angka in angka_ganjil:
    print(angka)
    
#28