a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))
c = int(input("Masukkan nilai c : "))
d = int(input("Masukkan nilai d : "))

pembilang = ( a * d ) + ( b * c )
penyebut = b * d

if pembilang == penyebut:
    sama = (pembilang/pembilang, penyebut/penyebut)
    print("Hasil = ",sama)
else:
    print("Hasil = ",pembilang,penyebut)

print("\n\n")




