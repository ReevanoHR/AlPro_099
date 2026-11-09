from random import sample

lotre = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
)

tiket_saya = [1, 5, "A", "D"]

percobaan = 0

while True:
    percobaan += 1

    tiket_pemenang = sample(lotre, 4)

    if tiket_pemenang == tiket_saya:
        break

print("Tiket saya menang!")
print(
    f"Dibutuhkan {percobaan} percobaan "
    "sebelum tiket saya menang."
)