menu_restoran = (
    "Nasi Goreng",
    "Mie Goreng",
    "Sate Ayam",
    "Bakso",
    "Soto Ayam"
)

print("Menu awal restoran:")
for makanan in menu_restoran:
    print(makanan)

#Menu tuple tidak dapat diubah, tetapi kita dapat membuat tuple baru dengan item yang diperbarui
print("\nMenu telah diperbarui!")

menu_restoran = (
    "Nasi Goreng",
    "Mie Goreng",
    "Rendang",
    "Gado-Gado",
    "Soto Ayam"
)

#menu restoran yang diperbarui maka akan menampilkan menu baru
for makanan in menu_restoran:
    print(makanan)