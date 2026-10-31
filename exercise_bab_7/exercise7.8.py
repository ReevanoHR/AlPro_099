pesanan_sandwich = [
    "tuna",
    "ayam",
    "telur"
]

sandwich_selesai = []

while pesanan_sandwich:
    pesanan = pesanan_sandwich.pop()

    print(
        f"Saya sedang membuat sandwich {pesanan}."
    )

    sandwich_selesai.append(pesanan)

print("\nSandwich yang telah selesai:")

for sandwich in sandwich_selesai:
    print(sandwich)