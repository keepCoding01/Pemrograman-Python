def add(Angka1, Angka2):
    res_angka1 = str(Angka1)[::-1]
    res_angka2 = str(Angka2)[::-1]
    jumlah = Angka1 + Angka2
    print("Reserve angka 1 : ", int(res_angka1))
    print("Reserve Angka 2 : ", int(res_angka2))
    return jumlah


Angka1 = int(input("Masukkan nilai angka pertama : "))
Angka2 = int(input("Masukkan nilai angka kedua : "))

jumlah = add(Angka1, Angka2)
print("total =", jumlah)
