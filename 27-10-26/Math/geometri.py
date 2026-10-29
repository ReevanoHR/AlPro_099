import statistics

def nilaiStatistik(listnilai):


    mean = statistics.mean(listnilai)
    median = statistics.median(listnilai)
    mode = statistics.mode(listnilai)
    stdev = statistics.stdev(listnilai)

    return mean, median, mode, stdev

#Jadi sebenernya bisa ngecheat dengan cara melihat dalam modul statistics, tapi kalau mau bikin sendiri juga bisa.

import math

def akar_kuadrat(n):
    return math.hypot(n, 0)

def pangkat(n, exp):
    return math.pow(n, exp)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def luas_segitiga(alas, tinggi):
    Luas = 0.5 * alas * tinggi
    return Luas

def luas_lingkaran(jari_jari):
    Luas = math.pi * jari_jari ** 2
    return Luas

def volume_tabung(Luas, tinggi):
    volume = Luas * tinggi
    return volume

def main():
    jari2 = float(input("Masukkan jari-jari lingkaran: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    VolTabung = volume_tabung(luas_lingkaran(jari2), tinggi)
    print(VolTabung)
    
#print(__name__) #ketika dianggil ke file lain maka akan menampilkan nama file, tapi kalau dijalankan langsung maka akan menampilkan __main__
if __name__ == "__main__":
    main()
