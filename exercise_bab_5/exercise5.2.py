nama = "Reev"
umur = 18
buah = ["apel", "jeruk", "mangga"]

# Equality dan inequality dengan string
print("Pengujian string:")
print(nama == "Reev")      # True
print(nama == "Andi")      # False
print(nama != "Andi")      # True
print(nama != "Reev")      # False

# Menggunakan lower()
print("\nPengujian lower():")
print(nama.lower() == "reev")    # True
print(nama.lower() == "andi")    # False

# Pengujian numerik
print("\nPengujian numerik:")
print(umur == 18)         # True
print(umur != 20)         # True
print(umur > 17)          # True
print(umur < 17)          # False
print(umur >= 18)         # True
print(umur <= 15)         # False

# Menggunakan and
print("\nPengujian and:")
print(umur > 15 and umur < 20)   # True
print(umur > 20 and umur < 30)   # False

# Menggunakan or
print("\nPengujian or:")
print(umur < 10 or umur == 18)   # True
print(umur < 10 or umur > 30)    # False

# Item ada dalam list
print("\nPengujian keanggotaan list:")
print("apel" in buah)            # True
print("pisang" in buah)          # False

# Item tidak ada dalam list
print("\nPengujian tidak ada dalam list:")
print("pisang" not in buah)      # True
print("apel" not in buah)        # False