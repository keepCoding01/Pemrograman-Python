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
