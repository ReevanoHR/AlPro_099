import math
from datetime import datetime


def tarif_parkir(jenis, masuk, keluar):
    tanggal_masuk, jam_masuk = masuk.split()
    tanggal_keluar, jam_keluar = keluar.split()

    hari1, bulan1, tahun1 = map(int, tanggal_masuk.split("-"))
    jam1, menit1 = map(int, jam_masuk.split(":"))

    hari2, bulan2, tahun2 = map(int, tanggal_keluar.split("-"))
    jam2, menit2 = map(int, jam_keluar.split(":"))

    waktu1 = datetime(tahun1, bulan1, hari1, jam1, menit1)
    waktu2 = datetime(tahun2, bulan2, hari2, jam2, menit2)

    durasi = waktu2 - waktu1
    jam = durasi.days * 24 + durasi.seconds // 3600

    if durasi.total_seconds() <= 0:
        return "Waktu parkir tidak valid!"

    if jenis == "becak":
        tarif = 1000

    elif jenis == "motor":
        tarif = 2000
        if jam > 2:
            tarif = tarif + (jam - 2) * 1000
        if tarif > 10000:
            tarif = 10000

    elif jenis == "mobil":
        tarif = 4000
        if jam > 2:
            tarif = tarif + (jam - 2) * 2000
        if tarif > 15000:
            tarif = 15000

    else:
        return "Jenis kendaraan tidak valid!"

    return tarif
