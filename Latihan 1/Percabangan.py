# nomor 1
import numpy as np

num = input("Tekan Tombol : ").split()

alpha = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], [
    "m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

for hasil in num:
    if int(hasil) == 1:
        print()
    if hasil == "*":
        print()
    if hasil == "#":
        print()
    if int(hasil) == 0:
        print(" ", end="")

    if int(hasil) == 2:
        print(alpha[0][0], end="")
    if int(hasil) == 22:
        print(alpha[0][1], end="")
    if int(hasil) == 222:
        print(alpha[0][2], end="")

    if int(hasil) == 3:
        print(alpha[1][0], end="")
    if int(hasil) == 33:
        print(alpha[1][1], end="")
    if int(hasil) == 333:
        print(alpha[1][2], end="")

    if int(hasil) == 4:
        print(alpha[2][0], end="")
    if int(hasil) == 44:
        print(alpha[2][1], end="")
    if int(hasil) == 444:
        print(alpha[2][2], end="")

    if int(hasil) == 5:
        print(alpha[3][0], end="")
    if int(hasil) == 55:
        print(alpha[3][1], end="")
    if int(hasil) == 555:
        print(alpha[3][2], end="")

    if int(hasil) == 6:
        print(alpha[4][0], end="")
    if int(hasil) == 66:
        print(alpha[4][1], end="")
    if int(hasil) == 666:
        print(alpha[4][2], end="")

    if int(hasil) == 7:
        print(alpha[5][0], end="")
    if int(hasil) == 77:
        print(alpha[5][1], end="")
    if int(hasil) == 777:
        print(alpha[5][2], end="")
    if int(hasil) == 7777:
        print(alpha[5][3], end="")

    if int(hasil) == 8:
        print(alpha[6][0], end="")
    if int(hasil) == 88:
        print(alpha[6][1], end="")
    if int(hasil) == 888:
        print(alpha[6][2], end="")

    if int(hasil) == 9:
        print(alpha[7][0], end="")
    if int(hasil) == 99:
        print(alpha[7][1], end="")
    if int(hasil) == 999:
        print(alpha[7][2], end="")
    if int(hasil) == 9999:
        print(alpha[7][3], end="")

# nomor 2
data_mahasiswa = []
jumlah = int(input("Masukkan jumlah siswa yang akan diinput datanya : "))

for mahasiswa in range(1, jumlah+1):
    nim = input(f"Masukkan Nama ke-{mahasiswa} : ")
    nama = input(f"Masukkan Nim ke-{mahasiswa} : ")
    opk = input(f"Masukkan Nilai Matkul Otomasi : ")
    program = input(f"Masukkan NIlai Matkul Programming : ")
    leader = input(f"Masukkan Nilai Leadership : ")

    data_mahasiswa.append([nim, nama, opk, program, leader])

# bentuk listnya :

# print("\n")
# print("berikut data mahasiswa : ", "\n", data_mahasiswa)
# print("\n")


for i in range(len(data_mahasiswa)):
    print(f"{i+1}. {data_mahasiswa[i][0]} - {data_mahasiswa[i]
          [1]} - {data_mahasiswa[i][2]} - {data_mahasiswa[i][3]} - {data_mahasiswa[i][4]}")

nilai_tertinggi_opk = data_mahasiswa[0][2]
nilai_terendah_opk = data_mahasiswa[0][2]
nilai_tertinggi_program = data_mahasiswa[0][3]
nilai_terendah_program = data_mahasiswa[0][3]
nilai_tertinggi_leader = data_mahasiswa[0][4]
nilai_terendah_leader = data_mahasiswa[0][4]

for i in range(len(data_mahasiswa)):
    if data_mahasiswa[i][2] > nilai_tertinggi_opk:
        nilai_tertinggi_opk = data_mahasiswa[i][2]
    elif data_mahasiswa[i][2] < nilai_terendah_opk:
        nilai_terendah_opk = data_mahasiswa[i][2]
    if data_mahasiswa[i][2] > nilai_tertinggi_program:
        nilai_tertinggi_program = data_mahasiswa[i][3]
    elif data_mahasiswa[i][2] < nilai_terendah_program:
        nilai_terendah_program = data_mahasiswa[i][3]
    if data_mahasiswa[i][2] > nilai_tertinggi_leader:
        nilai_tertinggi_leader = data_mahasiswa[i][4]
    elif data_mahasiswa[i][2] < nilai_terendah_leader:
        nilai_terendah_leader = data_mahasiswa[i][4]

print("Nilai matkul otomasi tertinggi adalah", nilai_tertinggi_opk)
print("Nilai matkul otomasi terendah adalah", nilai_terendah_opk)
print("Nilai matkul pemrograman tertinggi adalah", nilai_tertinggi_program)
print("Nilai matkul pemrograman terendah adalah", nilai_terendah_program)
print("Nilai matkul leadership tertinggi adalah", nilai_tertinggi_leader)
print("Nilai matkul leadership terendah adalah", nilai_terendah_leader)
