nilai_tugas = float(input("Masukkan nilai tugas : "))
nilai_uts = float(input("Masukkan nilai uts : "))
nilai_uas = float(input("Masukkan nilai uas : "))
nilai_akhir = (nilai_tugas+nilai_uts+nilai_uas)/3

if nilai_akhir >= 100:
    print("Nilai A")
elif nilai_akhir > 85:
    print("Nilai B")
elif nilai_akhir >= 70:
    print("Nilai C")
elif nilai_akhir >= 55:
    print("Nilai D")
elif nilai_akhir >= 40:
    print("Nilai E")
else:
    print("Nilai F")
