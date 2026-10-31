pesan_terkirim = []
pesan_belum_terkirim = [
    "Halo",
    "Belajar Python",
    "Dictionary"
]

while pesan_belum_terkirim:
    pesan = (
        pesan_belum_terkirim.pop()
    )

    pesan_terkirim.append(
        pesan
    )

print(pesan_terkirim)