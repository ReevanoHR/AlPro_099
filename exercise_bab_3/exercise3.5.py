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