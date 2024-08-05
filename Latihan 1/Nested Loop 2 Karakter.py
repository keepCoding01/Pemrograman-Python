n = int(input("Masukkan angka anda : "))

# Loop utama untuk setiap baris
for i in range(1, n ):
    # Loop kedua untuk karakter @
    for j in range(i):
        print('@', end='')
    
    # Loop ketiga untuk karakter +
    for k in range(n - i):
        print('+', end='')
    
    # Pindah ke baris berikutnya setelah mencetak baris saat ini
    print()



    # Menentukan jumlah baris
n = int(input("Masukkan angka anda : "))
baris = 1

# Loop utama untuk setiap baris
while baris < n:
    kolom = 0
    
    # Loop untuk karakter @
    while kolom < baris:
        print('@', end='')
        kolom += 1
    
    # Loop untuk karakter +
    while kolom < n :
        print('+', end='')
        kolom += 1
    
    # Pindah ke baris berikutnya setelah mencetak baris saat ini
    print()
    baris += 1

