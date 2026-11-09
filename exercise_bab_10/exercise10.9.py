nama_file = [
    "cats.txt",
    "dogs.txt"
]

for file in nama_file:
    try:
        with open(file) as f:
            print(f.read())

    except FileNotFoundError:
        pass