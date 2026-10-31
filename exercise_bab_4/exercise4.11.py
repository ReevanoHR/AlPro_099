daftar_pizza = ["Pepperoni", "Keju", "Daging Sapi"]

teman_pizza = daftar_pizza[:]

daftar_pizza.append("Ayam BBQ")
teman_pizza.append("Seafood")

print("Pizza favorit saya:")
for pizza in daftar_pizza:
    print(pizza)

print("\nPizza favorit teman saya:")
for pizza in teman_pizza:
    print(pizza)
    
#33