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
    
print("=" * 50)

kelipatan_tiga = range(3, 31, 3)

for angka in kelipatan_tiga:
    print(angka)
    
print("=" * 50)

daftar_kubus = []

for angka in range(1, 11):
    kubus = angka ** 3
    daftar_kubus.append(kubus)

for kubus in daftar_kubus:
    print(kubus)
    
print("=" * 50)

daftar_kubus = [angka ** 3 for angka in range(1, 11)]

print(daftar_kubus)