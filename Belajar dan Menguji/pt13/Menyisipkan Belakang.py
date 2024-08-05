# Membuat kelas Node untuk merepresentasikan simpul dalam double linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Membuat kelas LinkedList


class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan simpul baru ke bagian akhir double linked list
    def insert(self, data):
        newNode = Node(data)  # Membuat simpul baru dengan data yang diberikan

        if self.head is None:
            # Jika linked list masih kosong, simpul baru menjadi kepala linked list
            self.head = newNode
        else:
            # Jika linked list tidak kosong, mencari simpul terakhir
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next

            # Mengatur simpul baru sebagai simpul selanjutnya dari simpul terakhir
            lastNode.next = newNode
            newNode.prev = lastNode

    # Menampilkan double linked list
    def display(self):
        if self.head is None:
            print("Double linked list kosong")
            return

        currentNode = self.head
        print("Double linked list:")
        while currentNode:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
        print()


# Membuat objek linked list
linkedlist = LinkedList()

# Menambahkan simpul baru
linkedlist.insert(4)
linkedlist.insert(15)
linkedlist.insert(7)

# Menampilkan double linked list
linkedlist.display()
