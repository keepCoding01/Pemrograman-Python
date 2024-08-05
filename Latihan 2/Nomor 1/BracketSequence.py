def simpanValidasi(kurung):
    kumpulan = []

    for karakter in kurung:
        if karakter == '(':
            kumpulan.append(karakter)
        elif karakter == ')':
            if not kumpulan or kumpulan.pop() != '(':
                return False

    return not kumpulan


def jumlahValid(kurung):
    jumlah = 0

    for i in range(len(kurung)):
        valid = kurung[i:] + kurung[:i]

        if simpanValidasi(valid):
            jumlah += 1

    return jumlah


kurung = input("Masukkan urutan kurung : ")

print("Jumlah shift yang menunjukkan urutan kurung yang benar :",
      jumlahValid(kurung))
