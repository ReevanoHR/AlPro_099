pesanan_sandwich = [
    "pastrami",
    "tuna",
    "pastrami",
    "ayam",
    "pastrami",
    "telur"
]

print("Maaf, pastrami sedang habis.")

while "pastrami" in pesanan_sandwich:
    pesanan_sandwich.remove("pastrami")

print("\nPesanan yang tersedia:")

for pesanan in pesanan_sandwich:
    print(pesanan)
    
#71