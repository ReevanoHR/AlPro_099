import math
A = 89
AK = math.sqrt (A)
print("akar kuadrat dari", A, "adalah ", AK)
#bisa ditulis
print("akar kuadrat dari {A} adalah {AK}")
BC = pow (A, 3)
print(A, "pangkat 3 adalah", BC)

#Contoh 2

def luaspersegi(a = float, t = float): #caranya biar variabel tidak bertentangan ialah degan mendefinisikan variabl a dan t dengan tipe string yang kalian inginkan
    luas = a * t
    return luas

ls_persegi = luaspersegi("Prabowo Hebat ", 5)
print("Luas persegi adalah", ls_persegi) #tidak eror

def luassegitiga(a, t): #caranya biar variabel tidak bertentangan ialah degan mendefinisikan variabl a dan t dengan tipe string yang kalian inginkan
    luas = 0.5 * a * t
    return luas

ls_segitiga = luassegitiga(10, 5)
print("Luas segitiga adalah", ls_segitiga) #eror karena adanya numerik

#dipython pendefinisian hanya sebagai alat bantu saat coding
#Fungsi tanpa nilai balik

def cetakbiodata(nama, handphone, email):
    print("\n\nData Pengguna Program")
    print("="*21)
    print("Nama \t\t:", nama)
    print("Handphone\t:", handphone)
    print("Email\t\t:", email)
    
nama = "Reevano HR"
handphone = "812800******"
email = "reevano@example.com"
cetakbiodata(nama, handphone, email)

#Contoh
def hitung_statistik_nilai(listnilai):
    total = 0
    for nilai in listnilai:
        total = total + nilai
    rataan = total / len(listnilai)
    #rataan = sum(listnilai)/len(listnilai) -->cara alternatif
    #rataan = stat.mean(listnilai) -->cara alternatif
    variasi = sum((x-rataan)**2 for x in listnilai) / len(listnilai)
    #variasi = stat.variance(listnilai) -->cara alternatif
    stddev = variasi ** 0.5 #

#fungsi 3

def volTabung(jari, tinggi):
    #global pi ---> dengan menambahkan kode ini maka variabel pi bisa dikenal secara global
    pi = 3.14 #varibel lokal, hanya bisa diakses dalam lingkungan ini saja. sampai return
    volume = pi * (jari ** 2) * tinggi
    return volume

volTabung(7, 10)
print(volTabung)