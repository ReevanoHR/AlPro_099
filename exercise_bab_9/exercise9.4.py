#class Restaurant

class restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} adalah restaurant yang menyajikan gaya masakan {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka.")
        
    #tambahan method
    def set_number_served(self, jumlah):
        self.number_served = jumlah
        
    def increment_number_served(self, tambahan):
        self.number_served += tambahan
        
restaurant1 = restaurant("Rumah Makan Padang", "Padang", 0)
print(f'Nama Restaurant: {restaurant1.restaurant_name}')
print(f'Jenis Masakan: {restaurant1.cuisine_type}')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print(f'Jumlah pelanggan yang dilayani: {restaurant1.number_served}')
print('Mengubah jumlah pelanggan yang dilayani menjadi 10')
restaurant1.set_number_served(10)
print(f'Jumlah pelanggan yang dilayani: {restaurant1.number_served}')
print('Menambahkan jumlah pelanggan yang dilayani sebanyak 5')
restaurant1.increment_number_served(5)
print(f'Jumlah pelanggan yang dilayani: {restaurant1.number_served}')
