from random import randint


class Dadu:
    def __init__(self, sisi=6):
        self.sisi = sisi

    def roll_die(self):
        print(randint(1, self.sisi))


print("Dadu 6 sisi:")
dadu_6 = Dadu()

for _ in range(10):
    dadu_6.roll_die()

print("\nDadu 10 sisi:")
dadu_10 = Dadu(10)

for _ in range(10):
    dadu_10.roll_die()

print("\nDadu 20 sisi:")
dadu_20 = Dadu(20)

for _ in range(10):
    dadu_20.roll_die()