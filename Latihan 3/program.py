class Queue:
    def __init__(self, maksimalKapasitas):
        self.antrian = maksimalKapasitas
        self.antrianSekarang = 0
        self.data = []

    def kosong(self):
        return self.antrianSekarang == 0

    def penuh(self):
        return self.antrianSekarang == self.antrian

    def enqueue(self, dataBaru):
        if self.penuh():
            print("\Maaf antrian sudah penuh. Tidak dapat menambah data antrian!")
        else:
            self.data.append(dataBaru)
            self.antrianSekarang += 1
            print("\nData antrian: ", dataBaru, " berhasil ditambahkan\n")

    def dequeue(self):
        if self.kosong():
            print(
                "\nAntrian Anda masih kosong. gagal menghapus data antrian!")
            return None
        else:
            dataKeluar = self.data.pop(0)
            self.antrianSekarang -= 1
            print("\nData antrian: ", dataKeluar, " berhasil dihapus\n")
            return dataKeluar

    def nampilkanQueue(self):
        print("==================================================")
        print("|           List Data Antrian Saat Ini            |")
        print("==================================================\n")
        if self.kosong():
            print("Data antrian masih kosong\n")
        else:
            datalist = "\n".join(map(str, self.data))
            print("Data antrian :", datalist, end=" ")
            print("\n")

    def queue_info(self):
        print("======================================================")
        print("|         Informasi data antrian Saat Ini            |")
        print("======================================================\n")
        print("Kapasitas max antrian         : ", self.antrian)
        print("Banyak isi antrian sekarang   : ", self.antrianSekarang)
        print("\n >> Informasi antrian <<")
        if self.kosong():
            print("Data antrian masih kosong")
        else:
            print("Data antrian paling depan     :", self.data[0])
            print("Data antrian paling belakang  : ", self.data[-1])


class ProgramAntrian:
    def __init__(self):
        self.queue = Queue(50)

    def menuUtama(self):
        print("\n======================================")
        print("|  Program Antrian Tiket Kereta Api  |")
        print("======================================\n")
        print("Daftar Menu Layanan :")
        print("1. Menambah Data Antrian")
        print("2. Melihat List Data Antrian")
        print("3. Menghapus Data Antrian terdahulu")
        print("4. Melihat Data Informasi Antrian")
        print("5. Keluar Dari Program\n")

        pilihan = input("Masukkan nomor layanan yang anda dipilih : ")
        self.pilihMenu(pilihan)

    def pilihMenu(self, pilihanPengguna):
        if pilihanPengguna == '1':
            dataBaru = input("Masukkan data antrian anda : ")
            self.queue.enqueue(dataBaru)
        elif pilihanPengguna == '2':
            self.queue.nampilkanQueue()
        elif pilihanPengguna == '3':
            self.queue.dequeue()
        elif pilihanPengguna == '4':
            self.queue.queue_info()
        elif pilihanPengguna == '5':
            print("Program selesai. Terima kasih 😊")
            exit()
        else:
            print("Terjadi kesalahan. coba lagi yuk!")


if __name__ == "__main__":
    programAntrian = ProgramAntrian()

    while True:
        programAntrian.menuUtama()
