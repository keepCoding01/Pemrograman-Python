
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self):
        if self.head is None:
            print("Double linked list is empty.")
        else:
            target = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            del (target)

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


dllist = DoublyLinkedList()

dllist.insert(40)
dllist.insert(7)
dllist.insert(15)
dllist.insert(4)

print("Double linked list sebelum penghapusan:")
dllist.display()

dllist.delete()

print("Double linked list setelah penghapusan:")
dllist.display()
