

# Minta pengguna memasukkan jumlah baris dan kolom
n = int(input("Masukkan Jumlah baris dan Kolom: "))

# Menampilkan pola tanpa perulangan bertingkat
for i in range(1, n + 1):
    print('*' * i)



# Minta pengguna memasukkan jumlah baris dan kolom
n = int(input("Masukkan Jumlah baris dan Kolom: "))

# Menampilkan pola segitiga terbalik
for i in range(n, 0, -1):
    print("*" * i)



# Minta pengguna memasukkan jumlah baris dan kolom
n = int(input("Masukkan Jumlah baris dan Kolom: "))

# Menampilkan deret segitiga rata kanan
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * i
    print(spaces + stars)


# Minta pengguna memasukkan jumlah baris dan kolom
n = int(input("Masukkan Jumlah baris dan Kolom: "))

# Menampilkan deret segitiga rata kiri
for i in range(1, n + 1):
    spaces = " " * (i - 1)
    stars = "*" * (n - i + 1)
    print(spaces + stars)


# Minta pengguna memasukkan tinggi piramida
n = int(input("Masukkan angka : "))

# Membuat piramida
for i in range(1, n + 1):
    spasi = " " * (n - i)
    bintang = "*" * (i * 2)
    print(spasi + bintang)
