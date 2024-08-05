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
