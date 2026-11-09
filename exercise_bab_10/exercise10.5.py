while True:
    alasan = input(
        "Mengapa Anda suka pemrograman? "
        "(ketik 'q' untuk keluar): "
    )

    if alasan == "q":
        break

    with open("polling.txt", "a") as file:
        file.write(f"{alasan}\n")