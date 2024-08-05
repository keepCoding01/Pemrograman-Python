class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Node tidak ditemukan!")
            return

        new_node = Node(new_data)
        new_node.prev = prev_node
        new_node.next = prev_node.next

        if prev_node.next is not None:
            prev_node.next.prev = new_node
        prev_node.next = new_node

    def printList(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()


doublyLinkedList = DoublyLinkedList()
doublyLinkedList.head = Node(4)
node2 = Node(15)
node3 = Node(7)
node4 = Node(40)

doublyLinkedList.head.next = node2
node2.prev = doublyLinkedList.head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

print("Linked list awal: ")
doublyLinkedList.printList()

new_data = 25
prev_node = node2
doublyLinkedList.insert(prev_node, new_data)

print("Linked list setelah menyisipkan node baru: ")
doublyLinkedList.printList()
