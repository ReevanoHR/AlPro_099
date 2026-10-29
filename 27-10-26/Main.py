import Math.geometri as geo 
# atau bisa juga dengan from untuk meng-import sesuatu yang spesifik dari modul geometri
#from Math.geometri import luas_lingkaran, volume_tabung

def volume_tabung(jari_jari, tinggi):
    luas = geo.luas_lingkaran(jari_jari)
    volume = geo.volume_tabung(luas, tinggi)
    return volume

def main():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    VolTab = geo.volume_tabung(geo.luas_lingkaran(jari_jari), tinggi)
    #print("Volume tabung dengan jari-jari", jari_jari, "dan tinggi", tinggi, "adalah:", VolTabung)
    
    print("Volume Tabung", VolTab)
    
if __name__ == "__main__":
    main()