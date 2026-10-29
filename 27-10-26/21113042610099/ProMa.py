from MODUL import tarif_parkir

print("=== PROGRAM TARIF PARKIR ProMa ===")

jenis = input("Masukkan jenis kendaraan (becak/motor/mobil): ").lower()

masuk = input("Tanggal dan jam masuk (DD-MM-YYYY HH:MM): ")
keluar = input("Tanggal dan jam keluar (DD-MM-YYYY HH:MM): ")

hasil = tarif_parkir(jenis, masuk, keluar)

print("\n=== HASIL PARKIR ===")
print("Jenis kendaraan:", jenis.capitalize())

if isinstance(hasil, int):
    print("Total tarif parkir: Rp", format(hasil, ",").replace(",", "."))
else:
    print(hasil)

print("====================")
