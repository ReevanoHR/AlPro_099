aktif = True

while aktif:
    pesan = input("Masukkan sesuatu: ")

    if pesan == "quit":
        aktif = False
    else:
        print(pesan)