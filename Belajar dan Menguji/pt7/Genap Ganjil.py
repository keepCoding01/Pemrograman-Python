# Inisialisasi variabel
count_genap = 0
total_ganjil = 0

# Perulangan untuk menerima masukan bilangan
while True:
    angka = int(input("Masukkan bilangan bulat (0 untuk keluar): "))

    # Cek bilangan genap
    if angka % 2 == 0:
        count_genap += 1

    # Cek bilangan ganjil
    elif angka % 2 != 0:
        total_ganjil += angka

    # Berhenti jika bilangan yang dimasukkan adalah 0
    if angka == 0:
        break

# Menampilkan hasil
print("Jumlah kemunculan bilangan genap:", count_genap)
print("Total bilangan ganjil:", total_ganjil)
