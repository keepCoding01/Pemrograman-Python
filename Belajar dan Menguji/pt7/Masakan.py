menu = ["sate kambing", "gulai sapi", "rendang"]
masak1 = str(input("Masukkan Menu pertama anda       : "))
masak2 = str(input("Masukkan Menu kedua anda         : "))
masak3 = str(input("Masukkan Menu kedua anda         : "))
mulai = int(input("Masukkan waktu mulai memasak     : "))

durasiMasak1 = 0
durasiMasak2 = 0
durasiMasak3 = 0

for i in menu:
    if masak1 == "sate kambing":
        durasiMasak1 = 1
    if masak2 == "gulai sapi":
        durasiMasak2 = 3
    if masak3 == "rendang":
        durasiMasak3 = 2
    else:
        print("Menu tidak ada dalam daftar")

    jumlah = durasiMasak1 + durasiMasak2 + durasiMasak3

selesai = 11
while mulai < 5:
    siap = mulai + jumlah
    print("Perkiraan waktu selesai memasak  :", siap, "WIB")
    break
if mulai > 5:
    print("anda harus masak lebih cepat agar siap tepat waktu!")

print()
