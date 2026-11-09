nama = input("Masukkan nama Anda: ")

with open("guest.txt", "w") as file:
    file.write(nama)
