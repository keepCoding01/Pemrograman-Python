n = int(input("Masukkan n: "))  # Meminta user untuk memasukkan nilai n
deret = []  # Membuat list kosong untuk menyimpan deret angka genap

# Mengisi list deret dengan angka genap pertama sebanyak n
for i in range(1, n+1):
    angka = i * 3
    deret.append(angka)

# Menampilkan deret angka genap
print("deret :", end=" ")
for angka in deret:
    print(angka, end=", ")

# Menjumlahkan deret angka genap
jumlah = sum(deret)
print("\nJumlah deret:", jumlah)
