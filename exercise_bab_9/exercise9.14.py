from random import sample

lotre = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
)

tiket_pemenang = sample(lotre, 4)

print("Tiket lotre pemenang adalah:")

for item in tiket_pemenang:
    print(item)

print(
    "\nJika tiket Anda cocok dengan kombinasi ini, "
    "Anda memenangkan hadiah!"
)