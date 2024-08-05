teks = input("Masukkan sebuah teks atau kalimat: ")

# Menginisialisasi variabel untuk menghitung jumlah huruf vocal dan total karakter
count_vocal = 0
count_char = 0

# Melakukan perulangan untuk setiap karakter dalam teks
for char in teks:
    # Mengecek apakah karakter adalah huruf vocal
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        count_vocal += 1  # Menambahkan 1 ke jumlah huruf vocal

    count_char += 1  # Menambahkan 1 ke total karakter

# Menampilkan hasil
print("Jumlah huruf vocal dalam teks tersebut:", count_vocal)
print("Total karakter dalam teks tersebut:", count_char)
