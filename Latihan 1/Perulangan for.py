n = 5

# Mencetak pola bagian atas
for i in range(n, 0, -1):
    # Mencetak spasi sebelum angka
    for j in range(n, i, -1):
        print(" ", end="")

    # Mencetak angka menurun dari i hingga 1
    for j in range(i, 0, -1):
        print(j, end="")

    # Mencetak angka naik dari 2 hingga i
    for j in range(1, i + 1):
        print(j, end="")

    # Pindah ke baris berikutnya
    print()

# Mencetak pola bagian bawah
for i in range(1, n + 1):
    # Mencetak spasi sebelum angka
    for j in range(n, i, -1):
        print(" ", end="")

    # Mencetak angka menurun dari i hingga 1
    for j in range(i, 0, -1):
        print(j, end="")

    # Mencetak angka naik dari 2 hingga i
    for j in range(1, i + 1):
        print(j, end="")

    # Pindah ke baris berikutnya
    print()
