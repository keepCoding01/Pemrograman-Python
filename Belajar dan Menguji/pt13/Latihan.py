def nambahData(n, data):
    dll.insert(n, data)


def hapusData(data):
    for i in range(len(dll)-1):
        if dll[i] == data:
            del dll[i]


def selipkanData(dataPatokan, data):
    x = 0
    for i in range(len(dll)-1):
        if dll[i] == dataPatokan and x == 0:
            dll.insert(i+1, data)
            x += 1


print("="*50)
dll = [15, 8, 22, 1]
print("Data Awal : ", dll)

# ================================================================================
print("="*50)
print("NOMOR A")
print("Hasil penambahan data 17 di belakang data 22 : ")
nambahData(3, 17)
for i in dll:
    print(i, end=" ")
print("\n")

print("="*50)
print("NOMOR B")
print("Hasil penghapusan data 15 & 8 : ")
hapusData(15)
hapusData(8)
for i in dll:
    print(i, end=" ")
print("\n")

print("="*50)
print("NOMOR C")
print("Hasil penambahan data 7 setelah data 22 dan penambahan data 9 di awal linked list : ")
selipkanData(22, 7)

nambahData(0, 9)
for i in dll:
    print(i, end=" ")
print("\n")
