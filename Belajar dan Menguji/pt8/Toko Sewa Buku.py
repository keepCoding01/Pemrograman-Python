print("=================    DAFTAR BUKU   =======================")
print("  kode buku  |      judul buku      |    harga(perhari)   ")
print("     01          tips diet sehat            Rp.2000       ")
print("     02        belajar python dasar         Rp.5000       ")
print("     03         sinar ultraviolet           Rp.3000       ")
print("     04          cerdas berbahasa           Rp.5000       ")

print("=================   DATA PENYEWA   =======================")
nama = str(input("masukkan nama anda        : "))
kode = str(input("masukkan kode buku        : "))
judul = str(input("masukkan judul buku       : "))
hari = int(input("masukkan jumlah hari      : "))

if kode == "01":
    if judul == "tips diet sehat":
        harga = 2000
elif kode == "02":
    if judul == "belajar python dasar":
        harga = 5000
elif kode == "03":
    if judul == "sinar ultraviolet":
        harga = 3000
elif kode == "04":
    if judul == "cerdas berbahasa":
        harga = 5000
else:
    print("kode yang anda masukkan tidak terdaftar")

sewa = harga * hari
print("====================   STRUK    ==========================")
print("nama penyewa              : ", nama)
print("judul buku yang di pinjam : ", judul)
print("lama peminjaman           : ", hari, "hari")
print("total harga peminjaman    : ", sewa)

lagi = input("Apakah Anda ingin menyewa buku lagi? (ya/tidak) ")
while lagi == "ya":
    kode = str(input("masukkan kode buku        : "))
    judul = str(input("masukkan judul buku       : "))
    hari = int(input("masukkan jumlah hari      : "))

    if kode == "01":
        if judul == "tips diet sehat":
            harga = 2000
    elif kode == "02":
        if judul == "belajar python dasar":
            harga = 5000
    elif kode == "03":
        if judul == "sinar ultraviolet":
            harga = 3000
    elif kode == "04":
        if judul == "cerdas berbahasa":
            harga = 5000
    else:
        print("kode yang anda masukkan tidak terdaftar")

    sewa += harga * hari
    print("====================   STRUK    ==========================")
    print("nama penyewa              : ", nama)
    print("judul buku yang di pinjam : ", judul)
    print("lama peminjaman           : ", hari, "hari")
    print("total harga peminjaman    : ", sewa)

    lagi = input("Apakah Anda ingin menyewa buku lagi? (ya/tidak) ")

print("Terima kasih telah menggunakan layanan kami!")
