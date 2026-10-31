players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappe", "Erling Haaland"]

# Original list
print("Original list:")
print(players)

# Accessing an element
print("\nFavorite player:")
print(players[0])

# append()
players.append("Lamine Yamal")
print("\nAfter append:")
print(players)

# insert()
players.insert(2, "Jude Bellingham")
print("\nAfter insert:")
print(players)

# del
del players[1]
print("\nAfter del:")
print(players)

# pop()
removed_player = players.pop()
print(f"\nPopped player: {removed_player}")
print(players)

# remove()
players.remove("Neymar")
print("\nAfter remove:")
print(players)

# sorted()
print("\nTemporary alphabetical order:")
print(sorted(players))

# Original list remains unchanged
print("\nOriginal list:")
print(players)

# reverse()
players.reverse()
print("\nReversed list:")
print(players)

# Mengurutkan kembali ke urutan asli
players.sort()
print("\nSorted permanently:")
print(players)

# Urutan secara terbalik permanen
players.sort(reverse=True)
print("\nReverse alphabetical order:")
print(players)

# Jumlah Player
print(f"\nNumber of players in the list: {len(players)}")