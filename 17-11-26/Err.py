import sys

a = float(input("Input bilangan pertama : "))
b = float(input("Input bilangan Kedua   : "))

#Blok penanganan eksepsi/error
#Tidak semua program harus langsung dimasukkan kedalam blok ini, setelah menemukan bisa diprtimbangkan untuk masukkan ke dalam bloknya
try:
    hasil_bagi = a / b
    # 
except ZeroDivisionError:
    print("\nError: Bilangan pembagi tidak boleh Nol (0)")
    sys.exit(1)  # Keluar dari program dengan kode status 1 (menandakan ada error)
    
print("Bilangan Pertama : ", a)
print("Bilangan Kedua   : ", b)
print("a / b = ", hasil_bagi)