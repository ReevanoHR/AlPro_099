#class Restaurant

class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} adalah restaurant yang menyajikan gaya masakan {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka.")
        
restaurant1 = restaurant("Rumah Makan Padang", "Padang")
print(f'Nama Restaurant: {restaurant1.restaurant_name}')
print(f'Jenis Masakan: {restaurant1.cuisine_type}')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

#9.2 tambah 2 restaurant

restaurant2 = restaurant("Rumah Makan Mbah Djo", "Jawa")
restaurant3 = restaurant("La' Cuisine", "Perancis")

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()