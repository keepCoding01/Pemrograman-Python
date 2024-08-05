def jumlahDistinct(bilangan):
    return len(set(bilangan))


tanya = int(input("Banyak Test Case: "))
hasil = []

for i in range(tanya):
    banyakBilangan, minAngkaBeda = map(int, input(
        "Banyak bilangan, Minimal Angka yang Berbeda: ").split())
    bilangan = list(map(int, input("Daftar Bilangan: ").split()))
    distinct = jumlahDistinct(bilangan)

    if distinct < minAngkaBeda:
        hasil.append(f"Test Case - {i+1} Bad")
    elif distinct > minAngkaBeda:
        hasil.append(f"Test Case - {i+1} Average")
    else:
        hasil.append(f"Test Case - {i+1} Good")

for result in hasil:
    print(result)
