# soal no 1

print("Mikro Playlist")
print("===========================================================")
print("1. Register")
print("2. Login")
print("3. Keluar")
pilihan = int(input("Fitur yang ingin digunakan (1/2/3) : "))
print()


if (pilihan == 1):
    nama = input(str("Masukkan username anda : "))
    print("Anda telah berhasil login. Selamat datang kembali ya!")

    print("="*5, "Kumpulan Lagu", "="*5)
    print("1. Blinding Lights")
    print("2. Pesawat Kertas")
    print("3. Pesan Terakhir")
    print("4. Menghapus Jejakmu")
    print("5. Narco")

    hasil = []
    while True:
        tanya1 = input(
            str("Apakah anda ingin menambahkan lagu ke dalam queue ? (Y/N)"))
        if tanya1 == "Y":
            tanya2 = input(
                str("Lagu no berapa yang ingin ditambahkan ke dalam queue ? "))
            if tanya2 == "1":
                hasil.append("Blinding Lights")
            elif tanya2 == "2":
                hasil.append("Pesawat Kertas")
            elif tanya2 == "3":
                hasil.append("Pesan Terakhir")
            elif tanya2 == "4":
                hasil.append("Menghapus Jejakmu")
            elif tanya2 == "5":
                hasil.append("Narco")
            else:
                print("kode yang anda masukkan salah")
                print(hasil)
        elif tanya1 == "N":
            print("Terima kasih sudah memilih lagu pilihan anda")
            break


if (pilihan == 2):
    print("Hai selamat datang")
    print("Anda telah berhasil login. Selamat datang kembali ya!")

    print("="*5, "Kumpulan Lagu", "="*5)
    print("1. Blinding Lights")
    print("2. Pesawat Kertas")
    print("3. Pesan Terakhir")
    print("4. Menghapus Jejakmu")
    print("5. Narco")

    hasil = []
    while True:
        tanya1 = input(
            str("Apakah anda ingin menambahkan lagu ke dalam queue ? (Y/N)"))
        if tanya1 == "Y":
            tanya2 = input(
                str("Lagu no berapa yang ingin ditambahkan ke dalam queue ? "))
            if tanya2 == "1":
                hasil.append("Blinding Lights")
            elif tanya2 == "2":
                hasil.append("Pesawat Kertas")
            elif tanya2 == "3":
                hasil.append("Pesan Terakhir")
            elif tanya2 == "4":
                hasil.append("Menghapus Jejakmu")
            elif tanya2 == "5":
                hasil.append("Narco")
            else:
                print("kode yang anda masukkan salah")
                print(hasil)
        elif tanya1 == "N":
            print("Terima kasih sudah memilih lagu pilihan anda")
            break


if (pilihan == 3):
    print("Kamu telah keluar! Terima kasih sudah menggunakan playlist :)")


# soal no 2 ===============================================================================


jumlah_karung = int(input("Masukkan jumlah karung: "))
karung = []
muat = []
tidak_muat = []
berat_total = 0
lift = 0

for i in range(jumlah_karung):
    karung.append(int(input(f"Masukkan berat karung ke {i+1}: ")))

for karung in karung:
    if berat_total + karung <= 100:
        berat_total += karung
        muat.append(karung)
    else:
        tidak_muat.append(karung)

while tidak_muat:
    if berat_total + tidak_muat[-1] <= 100:
        berat_total += tidak_muat.pop()
        muat.append(karung)
    else:
        break

lift = len(muat) + 1

print(f"Jumlah kali lift turun-naik: {lift}")
