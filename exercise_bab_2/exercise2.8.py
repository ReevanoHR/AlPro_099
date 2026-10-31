name_first = "Reevano"
name_last = "Santoso"
full_name = f"{name_first} {name_last}"
print(f"Hello, {full_name}, Let's learn Python programming together!")

print("=" * 50)

print(f'{full_name}'.lower())
print(f'{full_name}'.upper())
print(f'{full_name}'.title())

print("=" * 50)

famous_person = "Reihold Niebuhr"
message = f"{famous_person} Once said, 'Forgiveness is the final form of love.'"
print(message)

print("=" * 50)

person = " Sermub "

print(f"|{person}|----->\tperson.lstrip()\t:{person.lstrip()}|\n\t\t\tperson.rstrip()\t:{person.rstrip()}|\n\t\t\tperson.strip()\t:{person.strip()}|")

print("=" * 50)

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))