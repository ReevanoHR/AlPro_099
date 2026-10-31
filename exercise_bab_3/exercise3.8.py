places = ["Tokyo", "Makkah", "Berlin", "Paris", "New Delhi"]

print("list:")
print(places)

# Urutan secara abjad (sementara)
print("\nDiatur secara abjad:")
print(sorted(places))

# Urutan masih sama
print("\nOriginal list still:")
print(places)

# Urutan terbalik (sementara)
print("\nReverse alphabetical:")
print(sorted(places, reverse=True))

# Urutan masih sama
print("\nOriginal list still:")
print(places)

# Urutan Terbalik permanen
places.reverse()
print("\nReversed list:")
print(places)

# Balik ke Urutan Asli
places.reverse()
print("\nBack to original:")
print(places)

# Permanen urutan secara abjad
places.sort()
print("\nSorted permanently:")
print(places)

# Permanen Urutan secara terbalik
places.sort(reverse=True)
print("\nReverse alphabetical permanently:")
print(places)

#20