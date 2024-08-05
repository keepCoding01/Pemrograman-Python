# # push, nambah elemen baru ke bagian top stack
# # pop, menghapus sebuah elemen dari bagian top stack dan mengembalikan nilainya
# # top, mengembalikan nilai dr elemen yg terdapat pd top stack
# # size, mengembalikan jumlah elemen yg terdapat dalam stack
# # isEmpty, mengecek apakah stack dalam keadaan kosong atau tidak

# # underflow mengeluarkan elemen dr stack kosong  -1/0
# # overflow memasukkan ekemen ke dalam stack yang sudah penuh [ size-1/ size ]

# # stok = []
# # print(stok)

# # stok.append(1)
# # stok.append(2)
# # print(stok)

# # stok.pop()
# # print(stok)

# # print("="* 10)

# # enqueue, menambahkan elemen baru ke bagian belakang queue
# # dequeue, menghapus elemen dr bagian depan queue dan mengembalikan nilai dr elemen yang dihpus
# # front, mengembalikan nilai dr elemen yang terdapat dibagian depan queue
# # size, mengembalikan jumlah elemen yang terdapat dalam queueu
# # isEmpty, mengecek apakah queue dalam keadaan kosong atau tidak

# # underflow, mengeluarkan elemen dr queue kosong
# # overflow, memasukkan elemen kedalam queue yg sudah penuh

# class listQueue:
#     def __init__(self):
#         self.items = []
#         self.size = 0

#     def enqueue(self, data):
#         self.items.append(data)
#         self.size += 1

#     def dequeue(self):
#         data = self.items.pop(0)
#         self.size -= 1
#         return data

#     def sizes(self):
#         return self.size

#     def peek(self):
#         return self.items[self.size-1]


# q = listQueue()
# q.enqueue(10)
# q.enqueue(3)
# q.enqueue(4)
# print(q.sizes())
# print(q.peek())

# # ========================================


# class listantrian:
#     # inisialisasi variabel
#     def __init__(self):
#         self.item = []
#         self.size = 0

#     # fungsi untuk menambah data
#     def enqueue(self, data):
#         self.item.append(data)  # menambahkan data kedalam list
#         # dengan menggunakan append
#         self.size += 1

#     # fungsi untuk menghapus data

#     def dequeue(self):
#         # menghapus elemen yang paling awal
#         data = self.item.pop(0)
#         self.size -= 1
#         return data

#     # fungsi untuk mencari jumlah data

#     def jumlah(self):
#         return (self.size)  # pali point 5


# antrian = listantrian()
# antrian.enqueue("Apel")
# antrian.enqueue("Jeruk")
# antrian.enqueue("Anggur")
# print(antrian.item)


# # menghapus antrian
# print(antrian.dequeue())
# print(antrian.item)


# # menampilkan jumlah antrian
# print(antrian.jumlah())

# ==============================================================================

# class listQueue:
#     def __init__(self):
#         self.items = []
#         self.size = 0

#     def enqueue(self, data):
#         self.items.append(data)
#         self.size += 1

#     def dequeue(self):
#         data = self.items.pop()
#         data = self.items.pop()
#         self.size -= 1
#         return data


# q = listQueue()
# q.enqueue(7)
# q.enqueue(10)
# q.enqueue(1)
# q.enqueue(23)
# print(q.dequeue())

# ===================================
db_endedqueue = [1, 2, 3]

db_endedqueue.insert(0, 10)
print("Penambahan dari depan :", db_endedqueue)
db_endedqueue.pop(0)
print("Penghapusan dari Depan:", db_endedqueue)
print()
db_endedqueue.append(4)
print("Penambahan dari Belakang:", db_endedqueue)
db_endedqueue.pop()
print("Penghapusan dari Belakang:", db_endedqueue)
print()
