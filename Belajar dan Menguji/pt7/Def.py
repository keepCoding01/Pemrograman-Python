def get_jurusan(nim):
    jurusan = nim[:3]

    if jurusan == '111':
        return 'Teknik Informatika'
    elif jurusan == '112':
        return 'Sistem Informasi'
    elif jurusan == '113':
        return 'Teknologi Informasi'
    else:
        return 'Jurusan tidak ditemukan'


def get_ketua_jurusan(nim):
    jurusan = nim[:3]

    if jurusan == '111':
        return 'Sunario Megawan, S.Kom., M.Kom.'
    elif jurusan == '112':
        return 'Yuni Marlina Saragih,  S.Kom., M.Kom.'
    elif jurusan == '113':
        return 'Wulan Sri Lestari, S.Kom., M.Kom.'
    else:
        return 'Ketua jurusan tidak ditemukan'


n = int(input("Jumlah mahasiswa: "))

for i in range(n):
    nim = input("NIM Mahasiswa ke-{}: ".format(i+1))
    nama = input("Nama Mahasiswa ke-{}: ".format(i+1))

    jurusan = get_jurusan(nim)
    ketua = get_ketua_jurusan(nim)

    print("Mahasiswa ke-{}:".format(i+1))
    print("- NIM:", nim)
    print("- Nama:", nama)
    print("- Jurusan:", jurusan)
    print("- Ketua Jurusan:", ketua)
    print()
