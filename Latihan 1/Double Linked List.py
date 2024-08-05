def nambahData(n, data):
    DoubleLinkedList.insert(n, data)


def hapusData(data):
    for i in range(len(DoubleLinkedList)-1):
        if DoubleLinkedList[i] == data:
            del DoubleLinkedList[i]


def selipkanData(dataBaru, data):
    x = 0
    for i in range(len(DoubleLinkedList)-1):
        if DoubleLinkedList[i] == dataBaru and x == 0:
            DoubleLinkedList.insert(i+1, data)
            x += 1


print("="*50)
DoubleLinkedList = [15, 8, 22, 1]
print("Data Awal : ", DoubleLinkedList)

# ================================================================================
print("="*50)
print(" NOMOR A")
print("Hasil penambahan data 17 di belakang data 22 : ")
nambahData(3, 17)
for i in DoubleLinkedList:
    print(i, end=" ")
print("\n")

print("="*50)
print("NOMOR B")
print("Hasil penghapusan data 15 & 8 : ")
hapusData(15)
'''
for i in DoubleLinkedList:
    print(i,end = " ")
print("\n")
'''
hapusData(8)
for i in DoubleLinkedList:
    print(i, end=" ")
print("\n")

print("="*50)
print("NOMOR C")
print("Hasil penambahan data 7 setelah data 22 dan penambahan data 9 di awal linked list : ")
selipkanData(22, 7)
'''
for i in DoubleLinkedList:
    print(i,end = " ")
print("\n")
'''
nambahData(0, 9)
for i in DoubleLinkedList:
    print(i, end=" ")
print("\n")
