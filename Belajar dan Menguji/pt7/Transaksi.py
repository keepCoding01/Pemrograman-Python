pelanggan1 = str(input("Masukkan kode pelanggan       : "))
jumlah1 = int(input("Masukkan jumlah pemakaian air : "))
pelanggan2 = str(input("Masukkan kode pelanggan       : "))
jumlah2 = int(input("Masukkan jumlah pemakaian air : "))
pelanggan3 = str(input("Masukkan kode pelanggan       : "))
jumlah3 = int(input("Masukkan jumlah pemakaian air : "))

for i in pelanggan1:
    if pelanggan1 == "F" and jumlah1 <= 50:
        biayaFU = 100
    elif jumlah1 > 50:
        biayaFU = 150
    elif jumlah1 > 100:
        biayaFU = 250
    else:
        print("Kode yang anda masukkan salah")

    if pelanggan2 == "R" and jumlah2 <= 50:
        biayaPB = 400
    elif jumlah2 > 50:
        biayaPB = 700
    elif jumlah2 > 100:
        biayaPB = 1000
    else:
        print("Kode yang anda masukkan salah")

    if pelanggan3 == "N" and jumlah3 <= 50:
        biayaN = 750
    elif jumlah3 > 50:
        biayaN = 1000
    elif jumlah3 > 100:
        biayaN = 1350
    else:
        print("Kode yang anda masukkan salah")

    print("\n")
    print("Biaya Fasilitas Umum adalah   : ", "Rp.", biayaFU * 1000)
    print("Biaya Perumahan Biasa adalah  : ", "Rp.", biayaPB * 1000)
    print("Biaya Niaga adalah            : ", "Rp.", biayaN * 1000)

print()

# izin pak, disini saya bingung, apakah dikali 1000 atau tidak pak.
# soalnya kemarin saya kumpul tanpa dikali seribu (sesuai yg ditabel soal),
# kata kak asdos nya dikali seribu. tapi ga tahu ini memang dikali seribu atau tidak, mohon bimbingan dan koreksinya pak
# terima kasih
