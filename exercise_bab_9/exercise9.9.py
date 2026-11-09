class Mobil:
    def __init__(
        self,
        pabrikan,
        model,
        tahun
    ):
        self.pabrikan = pabrikan
        self.model = model
        self.tahun = tahun


class Battery:
    def __init__(
        self,
        battery_size=40
    ):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 40:
            jarak = 150
        elif self.battery_size == 65:
            jarak = 225

        print(
            f"Mobil ini dapat menempuh sekitar {jarak} km."
        )

    def upgrade_battery(self):
        self.battery_size = max(self.battery_size, 65)


class MobilListrik(Mobil):
    def __init__(
        self,
        pabrikan,
        model,
        tahun
    ):
        super().__init__(
            pabrikan,
            model,
            tahun
        )

        self.battery = Battery()


mobil_saya = MobilListrik(
    "Tesla",
    "Model 3",
    2025
)

print("Sebelum upgrade:")
mobil_saya.battery.get_range()

mobil_saya.battery.upgrade_battery()

print("\nSetelah upgrade:")
mobil_saya.battery.get_range()