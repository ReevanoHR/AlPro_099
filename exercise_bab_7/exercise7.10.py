hasil_polling = {}

while True:
    nama = input("Nama Anda: ")
    tempat = input(
        "Jika bisa berlibur ke mana saja, ke mana Anda ingin pergi? "
    )

    hasil_polling[nama] = tempat

    lagi = input(
        "Apakah ada orang lain yang ingin mengisi? (ya/tidak): "
    )

    if lagi.lower() == "tidak":
        break

print("\nHasil polling:")

for nama, tempat in hasil_polling.items():
    print(
        f"{nama.title()} ingin berlibur ke {tempat.title()}."
    )