nim = str(input("Masukkan NIM : "))
nama_mhs = str(input("Masukkan nama : "))
dosen_wali = str(input("Masukkan wali : "))
tahun_ajaran = "2022/2023"

if nim[2:5] == "111":
    prodi = "Teknik Informatika"
elif nim[2:5] == "112":
    prodi = "Sistem Informasi"
elif nim[2:5] == "113":
    prodi = "Teknologi Informasi"
else:
    prodi = "N/A"

angkatan = "20" + nim[:2]

semester = int(tahun_ajaran[5:])-int(angkatan)

print("KARTU RENCANA STUDI")
print("FAKULTAS INFORMATIKA")
print("UNIVERSITAS MIKROSKIL")
print("T.A", tahun_ajaran)
print("=================================================")

print("nim : ", nim)
print("program studi : ", prodi)
print("nama : ", nama_mhs)
print("angkatan : ", angkatan)
print("Dosen wali : ", dosen_wali)
print("semester : ", semester)
print()
print("=================================================================")


# ------------------------------------------------------------------------------------------------------
# cara lain
nama = str(input("Masukkan nama\t\t\t: "))
NIM = str(input("Masukkan NIM\t\t\t: "))
dosen_wali = str(input("Nama Dosen Wali\t\t\t: "))
tahun_ajaran = "2023/2024"
angkatan = "20" + NIM[:2]
semester = (int(tahun_ajaran[5:]) - int(angkatan))
hari = str(input("Masukkan Hari\t\t\t: "))
kode = int(input("Masukkan Kode\t\t\t: "))
matkul = str(input("Masukkan Nama Mata Kuliah\t: "))
kelas = str(input("Masukkan Kelas\t\t\t: "))
ruangan = str(input("Masukkan Ruangan\t\t: "))
waktu = str(input("Masukkan Waktu\t\t\t: "))
sks = int(input("Masukkan Jumlah SKS\t\t: "))

if (NIM[2:5] == "111"):
    programStudi = "Teknik Informatika"
elif (NIM[2:5] == "112"):
    programStudi = "Sistem Informasi"
elif (NIM[2:5] == "113"):
    programStudi = "Teknologi Informasi"

print("=================================================================")

print("\t\t KARTU RENCANA STUDI")
print("\t\t FAKULTAS INFORMATIKA")
print("\t\t UNIVERSITAS MIKROSKIL")
print("=================================================================")

print("\n")

print("Nama\t\t: ", nama, "\tProgram Studi\t: ", programStudi)
print("NIM\t\t: ", NIM, "\tAngkatan\t: ", angkatan)
print("Nama Dosen Wali\t: ", dosen_wali, "\tSemester\t: ", semester)

print("\n")

print("\t\t\t\tTahun Ajaran\t: ", tahun_ajaran)

print("\n")

print("Hari\t\t\t\t: ", hari)
print("Kode\t\t\t\t: ", kode)
print("Nama Mata Kuliah\t\t: ", matkul)
print("Kelas\t\t\t\t: ", kelas)
print("Ruangan\t\t\t\t: ", ruangan)
print("Pukul\t\t\t\t: ", waktu)
print("SKS\t\t\t\t: ", sks)

print("\n")

print("============================selesai=============================")
