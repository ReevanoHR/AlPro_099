import sys ; salah = True

def inputData():
    try:
        a = float(input("Input bilangan pertama : "))
        b = float(input("Input bilangan Kedua   : "))
        return a, b
    except ValueError:
        print("\nError: Masukkan harus berupa angka")
        return None, None

#Blok penanganan eksepsi/error
#Tidak semua program harus langsung dimasukkan kedalam blok ini, setelah menemukan bisa diprtimbangkan untuk masukkan ke dalam bloknya\
while salah:
    a, b = inputData()
    try:
        hasil_bagi = a / b
        salah = False  # Keluar dari loop jika tidak ada error
    except ZeroDivisionError:
        print("\nError: Bilangan pembagi tidak boleh Nol (0)")
        clear = input("Tekan Enter untuk mengulang..")
        clearscreen = lambda: print("\033[H\033[J") # Fungsi untuk membersihkan layar terminal (opsional)
        clearscreen() # Membersihkan layar terminal
        # sys.exit(1)  # Keluar dari program dengan kode status 1 (menandakan ada error)
    
print("Bilangan Pertama : ", a)
print("Bilangan Kedua   : ", b)
print("a / b = ", hasil_bagi)