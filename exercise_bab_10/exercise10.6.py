try:
    angka_1 = int(input("Angka pertama: "))
    angka_2 = int(input("Angka kedua: "))

    print(angka_1 + angka_2)

except ValueError:
    print("Masukkan angka yang valid!")