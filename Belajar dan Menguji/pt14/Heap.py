def heapify(data, nilaiParentSekarang, indeksParentSekarang, jenis):
    maks = indeksParentSekarang
    kiri = 2 * indeksParentSekarang + 1
    kanan = 2 * indeksParentSekarang + 2

    if jenis == "max" and kiri < nilaiParentSekarang and data[kiri] > data[maks]:
        maks = kiri

    if jenis == "max" and kanan < nilaiParentSekarang and data[kanan] > data[maks]:
        maks = kanan

    if jenis == "min" and kiri < nilaiParentSekarang and data[kiri] < data[maks]:
        maks = kiri

    if jenis == "min" and kanan < nilaiParentSekarang and data[kanan] < data[maks]:
        maks = kanan

    if maks != indeksParentSekarang:
        data[indeksParentSekarang], data[maks] = data[maks], data[indeksParentSekarang]
        heapify(data, nilaiParentSekarang, maks, jenis)


def heap(data, jenis):
    nilaiParentSekarang = len(data)

    for indeksParentSekarang in range(nilaiParentSekarang // 2 - 1, -1, -1):
        heapify(data, nilaiParentSekarang, indeksParentSekarang, jenis)


def insert(data, value):
    data.append(value)

    nilaiParentSekarang = len(data)
    i = nilaiParentSekarang - 1
    parent = (i - 1) // 2

    while i > 0 and data[i] > data[parent]:
        data[i], data[parent] = data[parent], data[i]
        i = parent
        parent = (i - 1) // 2


def delete(data, value):
    index = data.index(value)
    data[index] = data[-1]
    data.pop()

    nilaiParentSekarang = len(data)
    i = index
    parent = (i - 1) // 2

    if data[i] > data[parent]:
        while i > 0 and data[i] > data[parent]:
            data[parent], data[i] = data[i], data[parent]
            i = parent
            parent = (i - 1) // 2
    else:
        heapify(data, nilaiParentSekarang, index, "max")


def menu():
    print("\nWelcome to Program Heap")
    print("1. Create Max Heap")
    print("2. Create Min Heap")
    print("3. Exit")
    pilihan = int(input("Masukkan pilihan fitur (1-3): "))
    opsi(pilihan)


def opsi(pilihan):
    data = []
    while pilihan < 3:
        if pilihan == 1:
            print("\nMasukkan data ke dalam heap")
            print("=" * 40)
            jumlahData = int(input("Jumlah Data : "))
            for i in range(jumlahData):
                masukkan = int(input(f"Input data ke-{i + 1}: "))
                data.append(masukkan)
            heap(data, "max")
            print("Max Heap:", data)

            while True:
                print("\nFitur Max Heap")
                print("=" * 40)
                print("1. Insert Data")
                print("2. Delete Data")
                print("3. Exit")
                fiturmax = int(
                    input("Masukkan pilihan fitur Max Heap (1-3): "))

                if fiturmax == 1:
                    print("\nMasukkan data ke dalam Heap")
                    print("=" * 40)
                    masukkan = int(input("Masukkan data: "))
                    insert(data, masukkan)
                    print("Max Heap:", data)

                elif fiturmax == 2:
                    hapus = int(input("\nData yang akan dihapus : "))
                    delete(data, hapus)
                    print(f"Data {hapus} telah dihapus")
                    print("Max Heap:", data)

                elif fiturmax == 3:
                    menu()
                    break

                else:
                    print("Invalid choice")

        elif pilihan == 2:
            print("\nMasukkan data ke dalam heap")
            print("=" * 40)
            jumlahData = int(input("Jumlah data : "))
            for i in range(jumlahData):
                masukkan = int(input(f"Input data ke-{i + 1}: "))
                data.append(masukkan)
            heap(data, "min")
            print("Min Heap:", data)

            while True:
                print("\nFitur Min Heap")
                print("=" * 40)
                print("1. Insert Data")
                print("2. Delete Data")
                print("3. Exit")
                fiturmin = int(
                    input("Masukkan pilihan fitur Min Heap (1-3): "))

                if fiturmin == 1:
                    print("\nMasukkan data ke dalam Min Heap")
                    print("=" * 40)
                    masukkan = int(input("Masukkan data : "))
                    insert(data, masukkan)
                    print("Min Heap:", data)

                elif fiturmin == 2:
                    hapus = int(input("\nData yang akan dihapus : "))
                    delete(data, hapus)
                    print(f"Data {hapus} telah dihapus")
                    print("Min Heap:", data)

                elif fiturmin == 3:
                    menu()
                    break

                else:
                    print("Pilihan tidak tersedia, silakan coba lagi")

        elif pilihan == 3:
            print("Program telah berakhir!")
        break


menu()
