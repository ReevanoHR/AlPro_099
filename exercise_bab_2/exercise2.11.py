#Program menampilkan nama lengkap
name_first = "Reevano"
name_last = "Santoso"
full_name = f"{name_first} {name_last}"
print(f"Hello, {full_name}, Let's learn Python programming together!")


#Program menebak angka favorit
fav = 99
guess = int(input("Guess my favorite number between 1 and 100: "))
if guess == fav:
    print(f"Congratulations! You guessed my favorite number! It99's {fav}.")
elif guess < fav:
    print("Wrong! My favorite number is higher than that.")
elif guess > fav:
    print("Wrong! My favorite number is lower than that.")
else:
    print("Invalid input. Please enter a number between 1 and 100.")
    
#11