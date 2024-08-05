# Minta pengguna untuk memasukkan jumlah baris dan kolom
jumlah_baris = int(input("Masukkan jumlah baris: "))
jumlah_kolom = int(input("Masukkan jumlah kolom: "))

# Loop untuk menghasilkan tabel perkalian
for baris in range(1, jumlah_baris + 1):
    for kolom in range(1, jumlah_kolom + 1):
        hasil = baris * kolom
        print(f"{baris} x {kolom} = {hasil}\t", end=' ')
    print()  # Pindah ke baris berikutnya setelah mencetak semua kolom

for i in range (1, jumlah_baris + 1):
    for j in range (1, jumlah_kolom + 1):
        hasil = i * j
        print(f"{i} x {j} = {hasil}\t", end= " ")
    print()


# Minta pengguna untuk memasukkan jumlah baris dan kolom
jumlah_baris = int(input("Masukkan jumlah baris: "))
jumlah_kolom = int(input("Masukkan jumlah kolom: "))

baris = 1

# Loop utama untuk menghasilkan tabel perkalian
while baris <= jumlah_baris:
    kolom = 1
    while kolom <= jumlah_kolom:
        hasil = baris * kolom
        print(f"{baris} x {kolom} = {hasil}\t", end=' ')
        kolom += 1
    print()  # Pindah ke baris berikutnya setelah mencetak semua kolom
    baris += 1



