places = ["Japan", "Iceland", "Switzerland", "New Zealand", "Canada"]

print("list:")
print(places)

# Alphabetical order (temporary)
print("\nDiatur secara abjad:")
print(sorted(places))

# Original list unchanged
print("\nOriginal list still:")
print(places)

# Reverse alphabetical order (temporary)
print("\nReverse alphabetical:")
print(sorted(places, reverse=True))

# Original list unchanged
print("\nOriginal list still:")
print(places)

# Reverse list permanently
places.reverse()
print("\nReversed list:")
print(places)

# Back to original order
places.reverse()
print("\nBack to original:")
print(places)

# Permanent alphabetical sort
places.sort()
print("\nSorted permanently:")
print(places)

# Permanent reverse alphabetical sort
places.sort(reverse=True)
print("\nReverse alphabetical permanently:")
print(places)