# deklarasi variabel dan tipe data
NAMA_KARTU = "KARTU PERPUSTAKAAN"
ALAMAT_PERPUSTAKAAN = "SMP NEGERI 4 DOLOK PANRIBUAN SIMALUNGUN"
NOMOR_ANTRIAN = int(input("Masukkan Nomor Antrian : "))
NAMA_SISWA = str(input("Masukkan Nama Siswa : "))
RUANG_KELAS = str(input("Masukkan Ruang kelas : "))
NOMOR_BUKU = str(input("Masukkan Nomor Buku : "))
HARI_PEMINJAMAN = str(input("Masukkan Hari Peminjaman : "))
TANGGAL_PEMINJAMAN = int(input("Masukkan Tanggal Peminjaman : "))
HARI_PENGEMBALIAN = str(input("Masukkan Hari Pengembalian : "))
TANGGAL_PENGEMBALIAN = int(input("Masukkan Tanggal Pengembalian : "))
JUDUL_BUKU = str(input("Masukkan Judul Buku : "))
KETERANGAN = str(input("Masukkan ket : "))

LAMA_PINJAM = TANGGAL_PENGEMBALIAN - TANGGAL_PEMINJAMAN


# menampilkan data
print("=============================================")
print(NAMA_KARTU)
print(ALAMAT_PERPUSTAKAAN)
print("=============================================")
print("NO \t:", NOMOR_ANTRIAN)
print("NAMA\t:", NAMA_SISWA)
print("KELAS\t:", RUANG_KELAS)
print("=============================================")
print("NO\t\t\t:", NOMOR_BUKU)
print("Hari Peminjaman \t:", HARI_PEMINJAMAN)
print("Tanggal Peminjaman\t:", TANGGAL_PEMINJAMAN)
print("Hari Pengembalian \t:", HARI_PENGEMBALIAN)
print("Tanggal Pengembalian\t:", TANGGAL_PENGEMBALIAN)
print("Lama Peminjaman \t:", LAMA_PINJAM)
print("Judul Buku \t\t:", JUDUL_BUKU)
print("Ket\t\t\t:", KETERANGAN)
