nama_file = "learning_python.txt"

try:
    with open(nama_file) as file:
        isi = file.read()

except FileNotFoundError:
    print(
        "File tidak ditemukan."
    )

else:
    jumlah = (
        isi.lower().count("python")
    )

    print(
        f"Kata 'python' muncul "
        f"{jumlah} kali."
    )