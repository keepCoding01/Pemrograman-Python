
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, prev_node, data):
        new_node = Node(data)
        if prev_node is None:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            if new_node.next is not None:
                new_node.next.prev = new_node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                break
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("\n")


def TambahData(X, Data):
    DoubleLinkedList.insert(X, Data)


def PenghapusanData(Data):
    DoubleLinkedList.delete(Data)


def PenyelipanData(DataSetelah, Data):
    prev_node = None
    current = DoubleLinkedList.head
    while current is not None:
        if current.data == DataSetelah:
            break
        prev_node = current
        current = current.next
    if current is not None:
        DoubleLinkedList.insert(prev_node, Data)


DoubleLinkedList = DoubleLinkedList()

# A
print("A")
print("Penambahan Data 17 di belakang data 22")
TambahData(3, 17)
DoubleLinkedList.display()

# B
print("B")
print("Penghapusan Data 15 & 8")
PenghapusanData(15)
PenghapusanData(8)
DoubleLinkedList.display()

# C
print("C")
print("Penambahan data 7 setelah data 22 dan penambahan data 9 di awal Linked list")
PenyelipanData(22, 7)
TambahData(0, 9)
DoubleLinkedList.display()
