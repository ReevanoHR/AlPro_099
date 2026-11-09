class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def describe_restaurant(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")


class IceCreamStand(Restoran):
    def __init__(self, nama_restoran, jenis_masakan):
        super().__init__(nama_restoran, jenis_masakan)
        self.flavors = [
            "Cokelat",
            "Vanila",
            "Stroberi",
            "Matcha"
        ]

    def tampilkan_rasa(self):
        print("Rasa es krim yang tersedia:")

        for rasa in self.flavors:
            print(f"- {rasa}")


gerai_es_krim = IceCreamStand(
    "Ice Cream Reev",
    "Es Krim"
)

gerai_es_krim.tampilkan_rasa()