temanku = ["Reevano", "Santoso", "Rizky", "Dimas", "Fajar"]
print(temanku[0])
print(temanku[1])
print(temanku[2])
print(temanku[3])
print(temanku[4]) #kalau ingin menampilkan semua elemen list, bisa menggunakan perulangan for

print("=" * 50)
#kalo mau cepet, bisa pake perulangan for
for teman in temanku:
    message = f"Hello, {teman}, Let's learn Python programming together!"
    print(message)
