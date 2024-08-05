total_harga = int(input("Masukkan total harga : "))
jumlah_bayar = int(input("Masukkan jumlah uang : "))
kembalian = jumlah_bayar-total_harga

uang50k = kembalian // 50000
sisa = kembalian % 50000
uang20k = sisa//20000
sisa %= 20000
uang10k = sisa // 10000
sisa %= 10000
uang5k = sisa//5000
sisa %= 5000
uang2k = sisa // 2000
sisa %= 2000
uang1k = sisa // 1000
sisa %= 1000
uang500 = sisa // 500
sisa %= 500
uang200 = sisa // 200
sisa %= 200
uang100 = sisa // 2000

print("Total harga : ", total_harga)
print("Total bayar : ", jumlah_bayar)
print("Total kembalian : ", kembalian)
print("Pecahan kembalian : ")
print(uang50k, "Lembar pecahan uang RP.50000")
print(uang20k, "Lembar pecahan uang Rp.20000")
print(uang10k, "Lembar pecahan uang Rp.10000")
print(uang5k, "Lembar pecahan uang Rp.5000")
print(uang2k, "Lembar pecahan uang Rp.2000")
print(uang1k, "Lembar pecahan uang Rp.1000")
print(uang500, "Lembar pecahan uang Rp.500")
print(uang200, "Lembar pecahan uang Rp.200")
print(uang100, "Lembar pecahan uang Rp.100")

# ---------------------------------------------------------------------------------
# cara lain
nama_toko = ("TOKO KELONTONG")
total_harga = int(input("Masukkan Total Harga Belanja\t\t: "))
jumlah_uang = int(input("Masukkan Jumlah Uang yang dibayarkan\t: "))

kembalian = jumlah_uang - total_harga

pecahan50rb = kembalian // 50000

kembalian %= 50000
pecahan20rb = kembalian // 20000

kembalian %= 20000
pecahan10rb = kembalian // 10000

kembalian %= 10000
pecahan5rb = kembalian // 5000

kembalian %= 5000
pecahan2rb = kembalian // 2000

kembalian %= 2000
pecahan1rb = kembalian // 1000

kembalian %= 1000
pecahan5ratus = kembalian // 500

kembalian %= 500
pecahan2ratus = kembalian // 200

kembalian %= 200
pecahan1ratus = kembalian // 100

kembalian = jumlah_uang - total_harga


print("==========================================")

print(nama_toko)
print("Total Harga Barang\t\t: ", total_harga)
print("Jumlah Uang yang dibayarkan\t: ", jumlah_uang)
print("Kembalian \t\t\t: ", kembalian)

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
