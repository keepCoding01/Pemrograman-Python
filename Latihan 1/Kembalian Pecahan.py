nama_toko = ("TOKO KELONTONG")
total_harga = int(input("Masukkan Total Harga Belanja\t\t: "))
jumlah_bayar = int(input("Masukkan Jumlah Uang yang dibayarkan\t: "))
kembalian = jumlah_bayar - total_harga

pecahan50rb = kembalian // 50000
sisa = kembalian%50000
pecahan20rb = sisa // 20000
sisa %= 20000
pecahan10rb = sisa // 10000
sisa %= 10000
pecahan5rb = sisa // 5000
sisa %= 5000
pecahan2rb = sisa // 2000
sisa %= 2000
pecahan1rb = sisa // 1000
sisa %= 1000
pecahan5ratus = sisa // 500
sisa %= 500
pecahan2ratus = sisa // 200
sisa %= 200
pecahan1ratus = sisa // 100

print("==========================================")

print(nama_toko)
print("Total Harga Barang\t\t: ",total_harga)
print("Jumlah Uang yang dibayarkan\t: ",jumlah_bayar)
print("Kembalian \t\t\t: ",kembalian)

print("==========================================")

print("Pecahan kembalian : ")
print(pecahan50rb, "lembar uang pecahan Rp.50.000")
print(pecahan20rb, "lembar uang pecahan Rp.20.000")
print(pecahan10rb, "lembar uang pecahan Rp.10.000")
print(pecahan5rb, "lembar uang pecahan Rp.5.000")
print(pecahan2rb, "lembar uang pecahan Rp.2.000")
print(pecahan1rb, "lembar uang pecahan Rp.1.000")
print(pecahan5ratus, "lembar uang pecahan Rp.500")
print(pecahan2ratus, "lembar uang pecahan Rp.200")
print(pecahan1ratus, "lembar uang pecahan Rp.100")

