teks = input("Masukkan teks yang ingin dienkripsi: ")
jumlah_geser = int(input("Masukkan jumlah pergeseran (bilangan bulat): "))

enskripsi = ""
for huruf in teks:
    if 'a' <= huruf <= 'z':
        geser_huruf = chr(
            ((ord(huruf) - ord('a') + jumlah_geser) % 26) + ord('a'))
    elif 'A' <= huruf <= 'Z':
        geser_huruf = chr(
            ((ord(huruf) - ord('A') + jumlah_geser) % 26) + ord('A'))
    else:
        geser_huruf = huruf
    enskripsi += geser_huruf

print("Teks terenkripsi: ", enskripsi)

# chr adalah tipe data yg digunakan untuk mengonversi bilangan bulat menjadi karakter yang sesuai.
# misal chr(65) akan menghasilkan A, karena kode bilangan bulat 65 adalah A.

# ord digunakan untuk mengonversi karakter menjadi bilangan bulat yang sesuai.
# misal ord A akan menghasilkan 65, karena karakter A memiliki kode A.
