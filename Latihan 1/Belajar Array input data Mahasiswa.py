# nomor 1
print("-"*26, "Nomor 1", "-"*26)
print("\n")

# inisial variabel
data_mahasiswa = []

# perulangan sekaligus per-inputan data
for mahasiswa in range(1, 4):
    nim = input(f"Masukkan Nama ke-{mahasiswa}      : ")
    nama = input(f"Masukkan Nim ke-{mahasiswa}       : ")
    umur = input(f"Masukkan Umur ke-{mahasiswa}      : ")
    alamat = input(f"Masukkan Alamat ke-{mahasiswa}    : ")

    # simpan data sementara
    data_mahasiswa.append([nim, nama, umur, alamat])

# cetak data
print("\n")
print("berikut data mahasiswa : ", "\n", data_mahasiswa)
print("\n")

# nomor 2
print("-"*26, "Nomor 2", "-"*26)
print("\n")

# data mahasiswa tambahan
mahasiswa_tambahan = ["Reza Rahardian",
                      "222113907", "17", "Jl.M.H. Thamrin No.140"]

# tambahkan data ke variabel data_mahasiswa
data_mahasiswa.append(mahasiswa_tambahan)

# update data
print("Data Update Mahasiswa : ", "\n", data_mahasiswa)
print("\n")

# nomor 3
print("-"*26, "Nomor 3", "-"*26)
print("\n")

print("Nama Data yang di Cari : ", data_mahasiswa[1])
