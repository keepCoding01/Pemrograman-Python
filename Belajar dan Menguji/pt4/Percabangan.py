nilai_tugas = float(input("Masukkan nilai tugas : "))
nilai_uts = float(input("Masukkan nilai uts : "))
nilai_uas = float(input("Masukkan nilai uas : "))
mean = (nilai_tugas+nilai_uts+nilai_uas)/3

if mean >= 55:
    print("siswa lulus")
