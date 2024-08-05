
# Membuat class Node untuk merepresentasikan sebuah node dalam double linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Membuat class DoubleLinkedList untuk melakukan operasi pada double linked list


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node baru ke dalam double linked list dari bagian depan
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Menghapus node dari bagian belakang double linked list
    def delete(self):
        if self.head is None:
            print("Double linked list kosong")
            return

        current = self.head
        while current.next is not None:
            current = current.next

        if current.prev is None:  # Jika hanya satu node dalam double linked list
            self.head = None
        else:
            current.prev.next = None

    # Menampilkan double linked list
    def display(self):
        if self.head is None:
            print("Double linked list kosong")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Membuat objek dari class DoubleLinkedList
dllist = DoubleLinkedList()

# Menambahkan data ke dalam double linked list dari bagian depan
dllist.insert(40)
dllist.insert(7)
dllist.insert(15)
dllist.insert(4)

# Menampilkan double linked list sebelum menghapus node dari bagian belakang
dllist.display()

# Menghapus node dari bagian belakang
dllist.delete()

# Menampilkan double linked list setelah menghapus node dari bagian belakang
dllist.display()
