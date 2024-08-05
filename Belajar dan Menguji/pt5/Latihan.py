# studi kasus
Nim = str(input("Masukkan NIM : "))
Nama_Mahasiswa = str(input("Masukkan Nama : "))
Jurusan = str(input("Masukkan Jurusan : "))
Semester = int(input("Masukkan Semester : "))
kode_mtk = ["IF2101", "TI2103", "UM2101", "IF2102", "TI2102"]
matakuliah = ["Pemrograman Komputer", "S.Otomasi Perkantoran",
              "P.Karakter Kepemimpinan", "Wawasan Infomatika", "Pemikiran Desain"]
sks = [4, 4, 2, 4, 4]
nilai = ["A", "A", "A", "B", "C"]
total_sks = 0

print("\t\tUniversitas Mikroskil")
print("\t\tTahun Ajaran 2022/2023")
print("====================================================")
print("NIM\t : ", Nim)
print("Nama\t : ", Nama_Mahasiswa)
print("Jurusan\t : ", Jurusan)
print("Semester : ", Semester)
print()
print("____________________________________________________")
print("No   Kode     Mata kuliah\t\tSKS \tNilai")
print("____________________________________________________")
for i in range(5):
    print(i+1, " ", kode_mtk[i], " ", matakuliah[i],
          "\t", sks[i], "\t", nilai[i])
    total_sks += sks[i]
print("====================================================")
print("Total SKS : ", total_sks)
