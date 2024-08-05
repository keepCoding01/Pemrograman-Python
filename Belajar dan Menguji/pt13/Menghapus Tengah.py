# Membuat kelas untuk node dalam double linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Membuat kelas untuk double linked list


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node baru di bagian belakang linked list
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last

    # Menghapus node dengan data tertentu dari linked list
    def deleteNode(self, key):
        posisi = self.head

        # Menghapus node pertama jika node pertama merupakan node yang akan dihapus
        if posisi is not None and posisi.data == key:
            self.head = posisi.next
            if posisi.next is not None:
                posisi.next.prev = None
            posisi = None
            return

        # Mencari node dengan data tertentu
        while posisi:
            if posisi.data == key:
                break
            posisi = posisi.next

        # Jika node dengan data tertentu tidak ditemukan
        if posisi is None:
            return

        # Mengganti pointer dari node sebelum dan sesudahnya
        if posisi.prev is not None:
            posisi.prev.next = posisi.next
            if posisi.next is not None:
                posisi.next.prev = posisi.prev
        else:
            self.head = posisi.next
            if posisi.next is not None:
                posisi.next.prev = None

        posisi = None

    # Menampilkan double linked list
    def display(self):
        posisi = self.head
        while posisi:
            print(posisi.data, end=' ')
            posisi = posisi.next
        print()


# Membuat instance dari double linked list
dllist = DoubleLinkedList()

# Menambahkan node ke double linked list
dllist.push(4)
dllist.push(15)
dllist.push(7)
dllist.push(40)

print("Double Linked List awal:")
dllist.display()

# Menghapus node dengan data tertentu
data_hapus = 7
dllist.deleteNode(data_hapus)

print("\nDouble Linked List setelah menghapus node dengan data {}: ".format(data_hapus))
dllist.display()
