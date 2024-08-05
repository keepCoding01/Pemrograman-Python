uang = int(input("Masukkan jumlah uang : "))
bebek = 50000
potongan = 2000

n = int(input("Masukkan jumlah beli : "))

sisa_uang = uang - ((n*bebek) - (n*potongan))
print("Sisa uang anda adalah : ", sisa_uang)
