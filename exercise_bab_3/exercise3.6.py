guests = ["Albert Einstein", "Leonardo da Vinci", "Nikola Tesla"]

print(f"Dear {guests[0]}, I would be honored if you joined me for dinner.")
print(f"Dear {guests[1]}, I would be honored if you joined me for dinner.")
print(f"Dear {guests[2]}, I would be honored if you joined me for dinner.")

print("=" * 50)
print(f"\nUnfortunately, {guests[1]} can't make it to the dinner.")

guests[1] = "Isaac Newton"

print("\nNew invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored if you joined me for dinner.")
    
print("=" * 50)
print("\nI have found a bigger dinner table, so I can invite more guests.")

# Undangan tambahan
guests.insert(0, "Galileo Galilei")  # Add to the beginning
guests.insert(len(guests) // 2, "Charles Darwin")  # Add to the middle
guests.append("Eric Matthes")  # Add to the end

print("\nUpdated invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored if you joined me for dinner.")
    
print("=" * 50)
print("\nUnfortunately, the new dinner table won't arrive in time, and I can only invite two guests for dinner.")
